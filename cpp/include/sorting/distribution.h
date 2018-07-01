// -*- coding: utf-8 -*-
#pragma once


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
