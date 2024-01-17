#pragma once

#include <iostream>
#include <memory>
#include <string>
#include <unordered_map>
#include <set>
#include <queue>
#include <cstdlib> // For rand() and srand()
#include <ctime> // For time()
#include <chrono>

#include "../include/rocksdb/cache.h"
#include "../cache/cache_key.h"
#include "../include/rocksdb/db.h"
#include "../include/rocksdb/table.h"
#include "cachelib/allocator/CacheAllocator.h"
#include "folly/init/Init.h"
#include "../../db/db_impl/db_impl_secondary.h"
#include "util.h"
#include "cache_filter/cuckoofilter.h"

using ROCKSDB_NAMESPACE::Options;
using ROCKSDB_NAMESPACE::Slice;

using Cache = facebook::cachelib::LruAllocator; // or Lru2QAllocator, or TinyLFUAllocator
using DestructorData = typename Cache::DestructorData;
using DestructorContext = facebook::cachelib::DestructorContext;
using CacheConfig = typename Cache::Config;
using NVMCacheConfig = typename Cache::NvmCacheConfig;
using CacheKey = typename Cache::Key;
using CacheReadHandle = typename Cache::ReadHandle;
using cuckoofilter::CuckooFilter;
using cuckoofilter::HashUtil;


class CacheSet {
public:
    CacheSet() {}

    size_t GetSize() const {
        return cache_set.size();
    }


    void Insert(const CacheKey& cache_key) {
        uint32_t hash = HashUtil::SuperFastHash(CacheKeyToStr(cache_key));
        auto start_time = std::chrono::high_resolution_clock::now();
        cache_set.insert(hash);
        auto end_time = std::chrono::high_resolution_clock::now();
        auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end_time - start_time).count();
        std::cout << "cache_set_insert Time: " << duration << "us" << std::endl;
    }

    bool Check(const CacheKey& cache_key) {
        uint32_t hash = HashUtil::SuperFastHash(CacheKeyToStr(cache_key));
        auto start_time = std::chrono::high_resolution_clock::now();
        bool result = cache_set.find(hash) != cache_set.end();
        auto end_time = std::chrono::high_resolution_clock::now();
        auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end_time - start_time).count();
        std::cout << "cache_set_get Time: " << duration << "us" << std::endl;
        return result;
    }

    void Remove(const CacheKey& cache_key) {
        uint32_t hash = HashUtil::SuperFastHash(CacheKeyToStr(cache_key));
        auto start_time = std::chrono::high_resolution_clock::now();
        cache_set.erase(hash);
        auto end_time = std::chrono::high_resolution_clock::now();
        auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end_time - start_time).count();
        std::cout << "cache_set_remove Time: " << duration << "us" << std::endl;
    }

private:
    std::string CacheKeyToStr(const CacheKey& cache_key) {
        return std::string(cache_key.data(), cache_key.size());
    }

    std::set<uint32_t> cache_set;
};


class CacheFilter {
public:
    CacheFilter(uint64_t total_items) {
        filter = new CuckooFilter<uint32_t, 32>(total_items);
    }

    void Insert(const CacheKey& cache_key) {
        std::string key = CacheKeyToStr(cache_key);
        auto start_time = std::chrono::high_resolution_clock::now();
	std::unique_lock<std::shared_mutex> lock(mutex);
        if (filter->Add(HashUtil::SuperFastHash(key)) != cuckoofilter::Ok) {
            // std::cout << "Insert_failed, key: " << key << std::endl;
        }
        auto end_time = std::chrono::high_resolution_clock::now();
        auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end_time - start_time).count();
        // std::cout << "cache_filter_insert Time: " << duration << "us" << std::endl;
    }

    bool Check(const CacheKey& cache_key) {
        std::string key = CacheKeyToStr(cache_key);
        auto start_time = std::chrono::high_resolution_clock::now();
	std::shared_lock<std::shared_mutex> lock(mutex);
        auto result = filter->Contain(HashUtil::SuperFastHash(key));
        auto end_time = std::chrono::high_resolution_clock::now();
        auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end_time - start_time).count();
        // std::cout << "cache_filter_get Time: " << duration << "us" << std::endl;
        if (result != cuckoofilter::Ok) {
            // std::cout << "Check failed, key: " << key << std::endl;
            return false;
        }
        return true;
    }

    void Remove(const CacheKey& cache_key) {
        std::string key = CacheKeyToStr(cache_key);
        auto start_time = std::chrono::high_resolution_clock::now();
        std::shared_lock<std::shared_mutex> lock(mutex);
        if (filter->Delete(HashUtil::SuperFastHash(key)) != cuckoofilter::Ok) {
            // std::cout << "Remove_failed, key: " << key << std::endl;
        }
        auto end_time = std::chrono::high_resolution_clock::now();
        auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end_time - start_time).count();
        // std::cout << "cache_filter_remove Time: " << duration << "us" << std::endl;
    }

private:
    std::string CacheKeyToStr(const CacheKey& cache_key) {
        return std::string(cache_key.data(), cache_key.size());
    }

    std::shared_mutex mutex;
    CuckooFilter<uint32_t, 32>* filter;
};

class AdmissionQueue {
private:
    uint64_t maxSize;
    std::queue<uint64_t> keyQueue;
    std::set<uint64_t> keySet;

public:
    AdmissionQueue(uint64_t capacity) {
        maxSize = capacity;
    }

    bool check(uint64_t key) {
        auto setIt = keySet.find(key);
        if (setIt != keySet.end()) {
            return true;
        }
        return false;
    }

    void insert(uint64_t key) {
        if (keySet.find(key) != keySet.end()) {
            return;
        }
        if (keyQueue.size() == maxSize) {
            keySet.erase(keyQueue.front());
            keyQueue.pop();
        }
        keySet.insert(key);
        keyQueue.push(key);
    }
};

class AdmissionList {
private:
  uint64_t maxSize;
  std::list<uint64_t> keyList;
  std::set<uint64_t> keySet;

  void moveToFront(uint64_t key) {
    auto it = keyList.begin();
    while (it != keyList.end()) {
        if (*it == key) {
            keyList.splice(keyList.begin(), keyList, it);  // Move the element to the front
        }
        ++it;
    }
  }
  
public:
  AdmissionList(uint64_t capacity) {
    maxSize = capacity;
  }

  bool check(uint64_t key) {
    auto setIt = keySet.find(key);
    if (setIt != keySet.end()) {
        moveToFront(key);
        return true;
    }
    return false;
  }

  void insert(uint64_t key) {
    if(keySet.find(key) != keySet.end()) {
        return;
    }
    if(keyList.size() == maxSize) {
      keySet.erase(keyList.back());
      keyList.pop_back();
    }
    keySet.insert(key);
    keyList.push_front(key);
  }
};

class SimpleCache {
public:
    SimpleCache(unsigned long navy_size_mb, unsigned long dram_size_mb, bool enable_filter) {
        initializeCache(navy_size_mb, dram_size_mb, enable_filter);
        uint64_t total_item = navy_size_mb * 1024UL / 4;
	std::cout << "total_item: " << total_item << std::endl;
        if(enable_filter) {
            cache_filter_ = new CacheFilter(total_item);
	    cache_set_ = new CacheSet();
            // cache_filter_all_lookup_ = new CacheFilter(1310720);
        }
        else {
            cache_filter_ = nullptr;
	    cache_set_ = nullptr;
            // cache_filter_all_lookup_ = nullptr;
        }
    }

    ~SimpleCache() {
        destroyCache();
    }

    void initializeCache(unsigned long navy_size_mb, unsigned long dram_size_mb, bool enable_filter) {
        CacheConfig config;
        config
            .setCacheSize(dram_size_mb * 1024UL * 1024UL) //
            .setCacheName("My Use Case")
            .setAccessConfig(
                {25 /* bucket power */, 10 /* lock power */}) // assuming caching 20
                                                                // million items
            .validate(); // will throw if bad config
        NVMCacheConfig nvmConfig;
        nvmConfig.navyConfig.setBlockSize(4096);
        // Seed the random number generator with the current time
        srand(time(nullptr));

        // Generate a random number between 1000 and 1 (inclusive)
        int random_number = rand() % (1000 - 1 + 1) + 1;
        std::string NavyFileName = NavyFileNameBase + std::to_string(random_number);
        nvmConfig.navyConfig.setSimpleFile(NavyFileName,
                                        navy_size_mb * 1024UL *1024UL /*fileSize*/,
                                        false /*truncateFile*/);
        nvmConfig.navyConfig.blockCache().setRegionSize(16 * 1024UL * 1024UL); // 16MB

        config.enableNvmCache(nvmConfig);

        if(enable_filter) {
            auto itemDestructor = [&](const DestructorData& data) {
                if(data.context == DestructorContext::kEvictedFromNVM) {
                    CacheKey key = data.item.getKey();
		    // std::cout << "reach_here" << std::endl;
		    // if(cache_filter_->Check(key) == true) {
                    cache_filter_->Remove(key);
		    // }
                    // rocksdb::CacheKey block_key;
                    // memcpy(&block_key, key.data(), key.size());
                    // uint64_t file_num = block_key.GetFileNum();
                    // if(cache_filter_all_lookup_->Check(key)) {
                    //     std::cout << "file num: " << file_num << "is useful" << std::endl;
                    // }
                    // else {
                    //     std::cout << "file num " << file_num << " is useless" << std::endl;
                    // }
                }
            };
            config.setItemDestructor(itemDestructor);
        }

        gCache_ = std::make_unique<Cache>(config);
        defaultPool_ =
            gCache_->addPool("default", gCache_->getCacheMemoryStats().cacheSize);
    }

    void destroyCache() { gCache_.reset(); }

    CacheReadHandle get(CacheKey key) { return gCache_->find(key); }

    bool put(CacheKey key, const Slice& value) {
        auto handle = gCache_->allocate(defaultPool_, key, value.size());
        if (!handle) {
            std::cout << "Cache may fail to evict due to too many pending writes" << std::endl;
            return false; // cache may fail to evict due to too many pending writes
        }
        std::memcpy(handle->getMemory(), value.data(), value.size());
        gCache_->insertOrReplace(handle);
        return true;
    }

    bool remove(CacheKey key) {
        auto rr = gCache_->remove(key);
        if (rr == Cache::RemoveRes::kSuccess) {
            return true;
        }
        return false;
    }

    size_t Size() {
        size_t size = 0;
        for (auto itr = gCache_->begin(); itr != gCache_->end(); ++itr) {
            size++;
        }
        return size;
    }

    void DisPlay() {
        std::cout << "Current Cache Content: " << std::endl;
        for (auto itr = gCache_->begin(); itr != gCache_->end(); ++itr) {
            auto key = itr->getKey();
            auto data = reinterpret_cast<const char*>(itr->getMemory());
            std::cout << key << " -> " << data << '\n';
        }
    }

    CacheFilter* cache_filter_;
    CacheSet* cache_set_;
    // CacheFilter* cache_filter_all_lookup_;
private:
    std::unique_ptr<Cache> gCache_;
    facebook::cachelib::PoolId defaultPool_;

};


class LocalCache {
public:
  LocalCache(int navy_size_mb, int dram_size_mb, bool enable_cache_filter, bool enable_admission_list) {
    // Allocte the CacheLib
    cache_ = std::unique_ptr<SimpleCache>(new SimpleCache(navy_size_mb, dram_size_mb, enable_cache_filter));
    uint64_t ListSize = 100;
    if(enable_admission_list) {
        // admission_list_ = new AdmissionList(ListSize);
        admission_list_ = new AdmissionQueue(ListSize);
    }
    else {
        admission_list_ = nullptr;
    }
    false_count = 0;
    access_count = 0;
  }

  void RecordInvalidFiles(const std::string& db_name, const std::vector<uint64_t>& files) {
    (void)db_name;
    for(auto it = files.begin(); it != files.end(); ++it) {
        if(admission_list_ != nullptr) {
            TIMED_OPERATION(
                admission_list_->insert(*it),
                "List_Insert"
            );
        }
    }
  }

  void EvictInvalidBlocks(const std::vector<rocksdb::CacheKey>& blocks) {
    for(auto it = blocks.begin(); it != blocks.end(); ++it) {
        Erase(*it);
    }
  }

  void Get(const Slice& key, Slice& val) {
    CacheKey block_key(key.data(), key.size());
    PRINT_STRING("Get key size");
    PRINT_STRING(std::to_string(key.size()));
    access_count++;
    // std::cout << "access_count: " << access_count << std::endl;
    if(cache_->cache_filter_ != nullptr) {
        if(cache_->cache_filter_->Check(block_key) == false) {
            // std::cout << "Block Key: " << block_key << " is not in the cache" << std::endl;
            return;
        }
    }

    // directly use cachelib to fetch out the data
    auto start_time = std::chrono::high_resolution_clock::now();
    auto handle = cache_->get(block_key);
    auto end_time = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end_time - start_time).count();
    // std::cout << "CacheLib Get Time: " << duration << "us" << std::endl;

    if (handle) {
        rocksdb::CacheKey rocksdb_block_key;
        memcpy(&rocksdb_block_key, key.data(), key.size());
        uint64_t file_num = rocksdb_block_key.GetFileNum();
        file_num_access_count_[file_num]++;
        // if(access_count % 100000 == 0) {
        //     std::cout << "file_num_begin_access_count: " << access_count << std::endl;
        //     for(auto it = file_num_access_count_.begin(); it != file_num_access_count_.end(); it++) {
        //         std::cout << "file_num: " << it->first << " access_count: " << it->second << std::endl;
        //     }
        //     std::cout << "file_num_end" << std::endl;
        // }
        // std::cout << "get handle is valid" << std::endl;
        auto data = folly::StringPiece{reinterpret_cast<const char*>(handle->getMemory()), handle->getSize()};
        // std::cout << data << '\n';
        val = Slice(data.data(), data.size());
    }
    else {
        false_count++;
        // std::cout << "false_count" << false_count << std::endl;
    }
  }

  void Insert(const Slice& key, const Slice& block_content) {
    CacheKey block_key(key.data(), key.size());

    rocksdb::CacheKey rocksdb_block_key;
    memcpy(&rocksdb_block_key, key.data(), key.size());
    uint64_t file_num = rocksdb_block_key.GetFileNum();
    if(admission_list_ != nullptr) {
        bool exist = false;
        TIMED_OPERATION(
            exist = admission_list_->check(file_num), 
            "List_Check"
        );
        if(exist == true) {
            std::cout << "reduce_insert_to_as_cache" << std::endl;
            return;
        }
    }
    if(file_num_access_count_.find(file_num) == file_num_access_count_.end()) {
        file_num_access_count_[file_num] = 0;
    }

    if(cache_->cache_filter_ != nullptr) {
        if(cache_->cache_filter_->Check(block_key) == false) {
            cache_->cache_filter_->Insert(block_key);
        }
    }
    auto start_time = std::chrono::high_resolution_clock::now();
    if(!cache_->put(block_key, block_content)) {
        PRINT_STRING("cache may fail to evict due to too many pending writes");
    }
    auto end_time = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end_time - start_time).count();
    // std::cout << "CacheLib Insert Time: " << duration << "us" << std::endl;
  }

  void Erase(const rocksdb::CacheKey& key) {
    Slice slice_key = key.AsSlice();
    CacheKey block_key(slice_key.data(), slice_key.size());
    if(cache_->cache_filter_ != nullptr) {
        if(cache_->cache_filter_->Check(block_key) == false) {
            return;
        }
    }
    else {
        cache_->remove(block_key);
    }
    if(cache_->cache_filter_ != nullptr) {
        cache_->cache_filter_->Remove(block_key);
    }
  }

private: 
  std::unique_ptr<SimpleCache> cache_;
  // AdmissionList* admission_list_;
  AdmissionQueue* admission_list_;
  uint64_t false_count;
  uint64_t access_count;
  std::map<uint64_t, uint64_t> file_num_access_count_;
};
