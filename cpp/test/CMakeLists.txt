cmake_minimum_required(VERSION 2.6)
project(dsa-test)

include_directories(../include)
add_subdirectory(lib/googletest/googletest)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_custom_target(build-time-make-test-directory
  ALL COMMAND ${CMAKE_COMMAND} -E make_directory bin
)

add_executable(bin/test_sorting test_sorting.cpp)
target_link_libraries(bin/test_sorting gtest_main)
