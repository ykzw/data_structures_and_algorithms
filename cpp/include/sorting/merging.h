// -*- coding: utf-8 -*-
#pragma once


template<typename T>
void merge(std::vector<T> &src, int i, int i_end, int j, int j_end,
           std::vector<T> &dst, int k)
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
