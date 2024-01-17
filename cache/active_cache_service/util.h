#pragma once

#define TIMED_OPERATION(operation, operation_name) \
    do { \
        constexpr bool should_print = true; \
        auto start_time = std::chrono::high_resolution_clock::now(); \
        operation; \
        auto end_time = std::chrono::high_resolution_clock::now(); \
        auto duration = std::chrono::duration_cast<std::chrono::nanoseconds>(end_time - start_time).count(); \
        if (should_print) { \
            std::cout << operation_name << " took " << duration << " nanoseconds." << std::endl; \
        } \
    } while (false)

#include <iostream>

static bool util_print = false;
#define PRINT_STRING(str) if(util_print) {std::cout << "\033[1;31m" << str << "\033[0m" << std::endl;}
static std::string secondary_kDBPath = "/tmp/secondary_db/secondary_db";
static std::string NavyFileNameBase = "/nvme/cachelib/NavyStorage";
