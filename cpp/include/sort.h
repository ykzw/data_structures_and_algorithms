// -*- coding: utf-8 -*-

#pragma once

#include <vector>
#include <functional>
#include <algorithm>


template<typename T>
void STL_sort(std::vector<T> &A)
{
    std::sort(A.begin(), A.end());
}


template<typename T>
void insertion_sort(std::vector<T> &A)
{
    auto n = A.size();
    for (int i = 1; i < n; ++i) {
        auto a = A[i];
        auto j = i - 1;
        while (j >= 0 && a < A[j]) {
            A[j + 1] = A[j];
            --j;
        }
        A[j + 1] = a;
    }
}


template<typename T>
void selection_sort(std::vector<T> &A)
{
    auto n = A.size();
    for (int i = 0; i < n; ++i) {
        auto min_elem = A[i];
        auto min_idx = i;
        for (int j = i + 1; j < n; ++j) {
            if (A[j] < min_elem) {
                min_elem = A[j];
                min_idx = j;
            }
        }
        std::swap(A[i], A[min_idx]);
    }
}


template<typename T>
void bubble_sort(std::vector<T> &A)
{
    auto n = A.size();
    for (int i = 0; i < n; ++i) {
        for (int j = 1; j < n; ++j) {
            if (A[j - 1] > A[j]) {
                std::swap(A[j - 1], A[j]);
            }
        }
    }
}


template<typename T>
void bubble_sort_opt(std::vector<T> &A)
{
    auto n = A.size();
    while (n > 0) {
        int m = 0;
        for (int j = 1; j < n; ++j) {
            if (A[j - 1] > A[j]) {
                std::swap(A[j - 1], A[j]);
                m = j;
            }
        }
        n = m;
    }
}


template<typename T>
int hoare_partition(std::vector<T> &A, int lo, int hi)
{
    auto pivot = A[lo];
    int i = lo - 1;
    int j = hi + 1;
    while (i < j) {
        while (++i <= j && A[i] < pivot) { }
        while (i <= --j && A[j] > pivot) { }
        if (i < j) {
            std::swap(A[i], A[j]);
        }
    }
    return j;
}


template<typename T>
int lomuto_partition(std::vector<T> &A, int lo, int hi)
{
    auto pivot = A[hi];
    auto i = lo - 1;
    for (int j = lo; j < hi; ++j) {
        if (A[j] < pivot) {
            ++i;
            std::swap(A[i], A[j]);
        }
    }
    std::swap(A[++i], A[hi]);
    return i;
}


template<bool lomuto, typename T>
void rec_quicksort(std::vector<T> &A, int lo, int hi)
{
    if (lo < hi) {
        int p;
        if (lomuto) {
            p = lomuto_partition(A, lo, hi);
        } else {
            p = hoare_partition(A, lo, hi);
        }
        rec_quicksort<lomuto>(A, lo, p - lomuto);
        rec_quicksort<lomuto>(A, p + 1, hi);
    }
}


template<typename T>
void hoare_quicksort(std::vector<T> &A)
{
    rec_quicksort<false>(A, 0, A.size() - 1);
}


template<typename T>
void lomuto_quicksort(std::vector<T> &A)
{
    rec_quicksort<true>(A, 0, A.size() - 1);
}


template<typename T>
void merge(std::vector<T> &src, int i, int i_end, int j, int j_end, std::vector<T> &dst, int k)
{
    auto x = i < i_end ? src[i] : 0;
    auto y = j < j_end ? src[j] : 0;
    while ((i < i_end) && (j < j_end)) {
        if (x <= y) {
            dst[k] = x;
            if (++i < i_end) {
                x = src[i];
            }
        } else {
            dst[k] = y;
            if (++j < j_end) {
                y = src[j];
            }
        }
        ++k;
    }
    for (; i < i_end; ++i, ++k) {
        dst[k] = src[i];
    }
    for (; j < j_end; ++j, ++k) {
        dst[k] = src[j];
    }
}


template<typename T>
void merge_sort(std::vector<T> &A)
{
    int n = A.size();
    std::vector<T> B(n);

    int r;
    for (r = 1; r < n; r *= 2) {
        for (int i = 0; i < n; i += 2 * r) {
            int i_end = std::min(i + r, n);
            int j = i_end;
            int j_end = std::min(j + r, n);
            merge(A, i, i_end, j, j_end, B, i);
        }
        std::swap(A, B);
    }

    if ((__builtin_clz(r) & 1) == 0) {  // If the number of passes is odd
        std::swap(A, B);
    }
}


template<typename T>
void heapsort(std::vector<T> &A)
{
    auto siftdown = [&A](int i, int end) {
        auto x = A[i];
        int child = 2 * i + 1;
        while (child < end) {
            auto right = child + 1;
            if (right < end && A[right] > A[child]) {
                child = right;
            }
            if (x > A[child]) {
                break;
            }
            A[i] = A[child];
            i = child;
            child = 2 * i + 1;
        }
        A[i] = x;
    };

    std::make_heap(A.begin(), A.end());
    for (int n = A.size() - 1; n > 0; --n) {
        std::swap(A[0], A[n]);
        siftdown(0, n);
    }
}


template<typename T>
void radix_sort(std::vector<T> &A)
{
    auto n = A.size();
    std::vector<T> B(A);

    int nbits = sizeof(T) * 8;
    int base_bits = 8;
    int base = 1 << base_bits;
    int mask = base - 1;

    std::vector<int> counts(base);
    for (int i = 0; i < nbits; i += base_bits) {
        for (int j = 0; j < base; ++j) {
            counts[j] = 0;
        }

        for (int j = 0; j < n; ++j) {
            auto a = A[j];
            int d = (a >> i) & mask;
            ++counts[d];
        }

        int s = 0;
        for (int j = 0; j < base; ++j) {
            auto t = counts[j];
            counts[j] = s;
            s += t;
        }

        for (int j = 0; j < n; ++j) {
            auto a = A[j];
            int d = (a >> i) & mask;
            B[counts[d]] = a;
            ++counts[d];
        }
        std::swap(A, B);
    }
}
