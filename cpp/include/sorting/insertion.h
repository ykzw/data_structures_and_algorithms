// -*- coding: utf-8 -*-
#pragma once


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
