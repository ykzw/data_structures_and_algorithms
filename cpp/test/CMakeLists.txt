cmake_minimum_required(VERSION 2.6)
project(dsa-test)

include_directories(../include)
add_subdirectory(lib/googletest/googletest)

set (CMAKE_CXX_STANDARD 14)
set (CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(test_sort test_sort.cpp)
target_link_libraries(test_sort gtest_main)
