# SAS-Cache
SAS-Cache: A Semantic-Aware Secondary Cache for LSM-based Key-Value Stores

## Setup 

Before you start, you need to have cmake3.22.3 (or higher version). 

* Install CacheLib - follow the installation steps available on the CacheLib website (https://cachelib.org/docs/installation) according to your particular operating system.
* Install SAS-Cache - clone this repository: `git clone git@github.com:Tom-CaoZH/SAS-Cache.git` and first you should modify your path to cachelib in `build.sh` and then run `bash build.sh`.

Then you can run db_bench using the following flags to use SAS-Cache features:

1. *use_local_flash_cache*: "Use the local flash as the secondary cache";
2. *flash_cache_size*: "the size of local flash cache of SAS-Cache in MB";
3. *dram_cache_size*: "the size of local dram cache of SAS-Cache in MB";
4. *use_flash_cache_filter*: "whether use filter in local flash cache";
5. *enable_flash_admission_list*: "whether enable admission list of flash cache";
6. *enable_flash_evict_blocks*: "whether enable evict invalid blocks of flash cache";
7. *enable_flash_prefetch_files*: "whether enable prefetching compaction-generated files to flash cache";
