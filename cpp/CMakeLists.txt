cmake_minimum_required(VERSION 2.6)
project(dsa)

include_directories(include)
add_subdirectory(test)

set(CMAKE_C_COMPILER gcc)
set(CMAKE_CXX_COMPILER g++)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(CMAKE_CXX_FLAGS "-O3 -march=native")

add_custom_target(build-time-make-directory
  ALL COMMAND ${CMAKE_COMMAND} -E make_directory bin
)

add_executable(bin/sorting src/sorting.cpp)
