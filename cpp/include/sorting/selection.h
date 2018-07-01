// -*- coding: utf-8 -*-
#pragma once

#include <algorithm>


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
