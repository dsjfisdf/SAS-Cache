#pragma once


#include <iostream>
#include <memory>
#include <string>
#include <iostream>
#include <mutex>
#include <future>
#include "util.h"

#include "rocksdb/cache.h"
#include "rocksdb/secondary_cache.h"
#include "cache_local.h"

using ROCKSDB_NAMESPACE::Slice;
// const bool print = false;
// #define PRINT_STRING(str) if(print) {std::cout << "\033[1;31m" << str << "\033[0m" << std::endl;}

class CacheClientLocal {
 public:
  CacheClientLocal(const std::shared_ptr<rocksdb::SecondaryCache>& cache) : cache_(cache) {}

  ~CacheClientLocal() {}

  void KeyRangePrefetch(std::string db_name, std::vector<char> smallest_data, std::vector<char> largest_data, int32_t level) {
    rocksdb::Status s;
    rocksdb::DB *secondary_db;
    rocksdb::Options secondary_option;
    rocksdb::BlockBasedTableOptions table_options;
    table_options.use_shared_cache_key = true;
    rocksdb::LRUCacheOptions opts(4 * 1024 /* capacity */, 0 /* num_shard_bits */,
                        false /* strict_capacity_limit */,
                        0.5 /* high_pri_pool_ratio */,
                        nullptr /* memory_allocator */, rocksdb::kDefaultToAdaptiveMutex,
                        rocksdb::kDontChargeCacheMetadata);
    opts.secondary_cache = cache_;
    std::shared_ptr<rocksdb::Cache> cache = rocksdb::NewLRUCache(opts);
    table_options.block_cache = cache;


    secondary_option.table_factory.reset(
                      rocksdb::NewBlockBasedTableFactory(table_options));

    secondary_option.create_if_missing = true;

    srand(time(nullptr));
    int random_number = rand() % (1000 - 1 + 1) + 1;
    s = rocksdb::DB::OpenAsSecondary(secondary_option, db_name, secondary_kDBPath + std::to_string(random_number), &secondary_db);
    assert(s.ok());

    secondary_db->TryCatchUpWithPrimary();

    std::vector<Slice> content;
    Slice min_keys(smallest_data.data(), smallest_data.size());
    Slice max_keys(largest_data.data(), largest_data.size());
    secondary_db->GetBlockInKeyRange(rocksdb::ReadOptions(), level, min_keys, max_keys, content);
    secondary_db->Close();
  }

  void RecordInvalidFiles(std::string& db_name, std::vector<uint64_t>& files) {
    cache_->RecordInvalidFiles(db_name, files);
  }


  void EvictInvalidBlocks(std::vector<rocksdb::CacheKey> blocks) {
    cache_->EvictInvalidBlocks(blocks);
  }

private:  
  std::shared_ptr<rocksdb::SecondaryCache> cache_;
};
