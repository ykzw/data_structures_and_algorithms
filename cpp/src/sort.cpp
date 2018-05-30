// -*- coding: utf-8 -*-

#include <vector>
#include <algorithm>
#include <typeinfo>

#include "sort.h"
#include "myutil.h"



template<typename T> struct _type;
template<> struct _type<uint32_t> { static const std::string name() { return "uint32_t"; } };
template<> struct _type<uint64_t> { static const std::string name() { return "uint64_t"; } };


#define RUN(func, name)                         \
    {                                           \
        std::vector<T> B(A);                    \
        Timer t; t.start();                     \
        func(B);                                \
        t.stop();                               \
        std::cout << name << ": "               \
                  << t.elapsed_time()           \
                  << " s\n";                    \
    }


template<typename T>
void benchmark(int n)
{
    std::vector<T> A;
    for (int i = 0; i < n; ++i) {
        A.push_back(i);
    }
    std::random_shuffle(A.begin(), A.end());

    std::cout << "===== Sort " << n << " elements of type " << _type<T>::name() << " =====\n\n";

    if (n < (1 << 16)) {  // O(n^2) algorithms
        RUN(  insertion_sort, "  Insertion sort");
        RUN(  selection_sort, "  Selection sort");
        RUN(     bubble_sort, "     Bubble sort");
        RUN( bubble_sort_opt, "Opt. bubble sort");
    }
    RUN(        STL_sort, "        STL sort");
    RUN( hoare_quicksort, " Hoare quicksort");
    RUN(lomuto_quicksort, "Lomuto quicksort");
    RUN(      merge_sort, "      Merge sort");
    RUN(        heapsort, "        Heapsort");
    RUN(      radix_sort, "      Radix sort");

    std::cout << std::endl;
}



int main(int argc, char *argv[])
{
    int n;

    n = 1 << 14;
    benchmark<uint32_t>(n);
    benchmark<uint64_t>(n);

    n = 1 << 22;
    benchmark<uint32_t>(n);
    benchmark<uint64_t>(n);

    return 0;
}
