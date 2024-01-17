#pragma once

#include <array>
#include <cstddef>
#include <memory>

#include "cache/lru_cache.h"
#include "memory/memory_allocator.h"
#include "rocksdb/secondary_cache.h"
#include "rocksdb/slice.h"
#include "rocksdb/status.h"
#include "cachelib/allocator/CacheAllocator.h"
#include "folly/init/Init.h"
#include "cache/active_cache_service/cache_local.h"
#include "cache/cache_key.h"

namespace ROCKSDB_NAMESPACE {

class SecondaryCacheLocalResultHandle : public SecondaryCacheResultHandle {
 public:
  SecondaryCacheLocalResultHandle(void* value, size_t size)
      : value_(value), size_(size) {}
  virtual ~SecondaryCacheLocalResultHandle() override = default;

  SecondaryCacheLocalResultHandle(
      const SecondaryCacheLocalResultHandle&) = delete;
  SecondaryCacheLocalResultHandle& operator=(
      const SecondaryCacheLocalResultHandle&) = delete;

  bool IsReady() override { return true; }

  void Wait() override {}

  void* Value() override { return value_; }

  size_t Size() override { return size_; }

 private:
  void* value_;
  size_t size_;

};

class SecondaryCacheLocal : public SecondaryCache {

public:
  SecondaryCacheLocal();
  SecondaryCacheLocal(uint64_t flash_size_mb, uint64_t dram_size_mb, bool enable_cache_filter, bool enable_admission_list);
  // SecondaryCacheLocal(std::string& server_addr);

  virtual ~SecondaryCacheLocal() override;

  const char* Name() const override { return "SecondaryCacheLocal"; }

  Status Insert(const Slice& key, void* value,
                const Cache::CacheItemHelper* helper) override;

  Status DirectlyInsert(const Slice& key, const Slice& value) override;

  Status RecordInvalidFiles(const std::string& db_name, const std::vector<uint64_t>& files) override;


  Status EvictInvalidBlocks(const std::vector<CacheKey>& blocks) override;

  std::unique_ptr<SecondaryCacheResultHandle> Lookup(
      const Slice& key, const Cache::CreateCallback& create_cb, bool /*wait*/,
      bool advise_erase, bool& is_in_sec_cache) override;

  bool SupportForceErase() const override { return true; }

  void Erase(const Slice& key) override;

  void WaitAll(std::vector<SecondaryCacheResultHandle*> /*handles*/) override {}

  std::string GetPrintableOptions() const override;

private:
  std::unique_ptr<LocalCache> cache_;
  // std::mutex mutex_;
  std::shared_mutex rw_mutex;
};

} // ROCKSDB_NAMESPACE