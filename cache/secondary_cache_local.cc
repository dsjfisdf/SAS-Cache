#include "secondary_cache_local.h"

#include <algorithm>
#include <cstdint>
#include <memory>
#include <iostream>

#include "memory/memory_allocator.h"
#include "monitoring/perf_context_imp.h"
#include "util/compression.h"
#include "util/string_util.h"

using ROCKSDB_NAMESPACE::SecondaryCacheLocal;
using ROCKSDB_NAMESPACE::SecondaryCacheResultHandle;

namespace ROCKSDB_NAMESPACE {

    SecondaryCacheLocal::SecondaryCacheLocal() {
      uint64_t navy_size_mb = 5120;
      uint64_t dram_size_mb = 8;
      bool enable_cache_filter = false;
      bool enable_admmision_list = false;
      cache_ = std::unique_ptr<LocalCache>(new LocalCache(navy_size_mb, dram_size_mb, enable_cache_filter, enable_admmision_list));
    }

    SecondaryCacheLocal::SecondaryCacheLocal(uint64_t flash_size_mb, uint64_t dram_size_mb, bool enable_cache_filter, bool enable_admission_list) {
      cache_ = std::unique_ptr<LocalCache>(new LocalCache(flash_size_mb, dram_size_mb, enable_cache_filter, enable_admission_list));
    }

    SecondaryCacheLocal::~SecondaryCacheLocal() {}

    ROCKSDB_NAMESPACE::Status SecondaryCacheLocal::Insert(const Slice& key, void* value,
                    const Cache::CacheItemHelper* helper) {

        size_t size = (*helper->size_cb)(value);
        CacheAllocationPtr ptr = AllocateBlock(size, nullptr);

        ROCKSDB_NAMESPACE::Status s = (*helper->saveto_cb)(value, 0, size, ptr.get());
        if (!s.ok()) {
            return s;
        }
        Slice val(ptr.get(), size);

        // std::lock_guard<std::mutex> lock(mutex_);
        std::shared_lock<std::shared_mutex> lock(rw_mutex);
        cache_->Insert(key, val);

        PRINT_STRING("key: " + key.ToString());
        PRINT_STRING("key size: " + std::to_string(key.size()));
        PRINT_STRING("insert val: " + val.ToString());

        return ROCKSDB_NAMESPACE::Status::OK();
    }

    ROCKSDB_NAMESPACE::Status SecondaryCacheLocal::DirectlyInsert(const Slice& key, const Slice& value) {
        // std::lock_guard<std::mutex> lock(mutex_);
        std::shared_lock<std::shared_mutex> lock(rw_mutex);
        cache_->Insert(key, value);

        // PRINT_STRING("key: " + key.ToString());
        // PRINT_STRING("key size: " + std::to_string(key.size()));
        // PRINT_STRING("insert val: " + value.ToString());

        return ROCKSDB_NAMESPACE::Status::OK();
    }

    ROCKSDB_NAMESPACE::Status SecondaryCacheLocal::RecordInvalidFiles(const std::string& db_name, const std::vector<uint64_t>& files) {

        cache_->RecordInvalidFiles(db_name, files);
        return ROCKSDB_NAMESPACE::Status::OK();
    }

    ROCKSDB_NAMESPACE::Status SecondaryCacheLocal::EvictInvalidBlocks(const std::vector<CacheKey>& blocks) {

        cache_->EvictInvalidBlocks(blocks);
        return ROCKSDB_NAMESPACE::Status::OK();
    }

    std::unique_ptr<SecondaryCacheResultHandle> SecondaryCacheLocal::Lookup(
        const Slice& key, const Cache::CreateCallback& create_cb, bool /*wait*/,
        bool advise_erase, bool& is_in_sec_cache) {

        std::unique_ptr<SecondaryCacheResultHandle> handle;
        is_in_sec_cache = false;

        Slice block_content;

        PRINT_STRING("key: " + key.ToString());

        std::shared_lock<std::shared_mutex> lock(rw_mutex);
        cache_->Get(key, block_content);

        PRINT_STRING("content size: " + std::to_string(block_content.size()));
        PRINT_STRING("get val: " + block_content.ToString());

        if(block_content.empty()) return nullptr;

        CacheAllocationPtr ptr = AllocateBlock(block_content.size(), nullptr);
        size_t handle_value_charge = block_content.size();

        std::memcpy(ptr.get(), block_content.data(), block_content.size());

        ROCKSDB_NAMESPACE::Status s;
        void* value{nullptr};
        size_t charge{0};

        s = create_cb(ptr.get(), handle_value_charge, &value, &charge);

        if (advise_erase) {
            Erase(key);
        } else {
            is_in_sec_cache = true;
        }
        handle.reset(new SecondaryCacheLocalResultHandle(value, charge));
        return handle;
    }

    void SecondaryCacheLocal::Erase(const Slice& key) {

        // std::lock_guard<std::mutex> lock(mutex_);
        std::shared_lock<std::shared_mutex> lock(rw_mutex);
        (void)key;
        // cache_->Erase(key);
        return;
    }

    std::string SecondaryCacheLocal::GetPrintableOptions() const { return " "; }
}