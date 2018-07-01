// -*- coding: utf-8 -*-
#pragma once


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
