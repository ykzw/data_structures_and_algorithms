// -*- coding: utf-8 -*-

#include <cstdint>
#include <vector>
#include <algorithm>
#include <gtest/gtest.h>

#include "sorting/sorting.h"


namespace {

    class SortingTest: public ::testing::Test {
    protected:
        SortingTest(): n(1 << 10) {
            for (int i = 0; i < n; ++i) {
                A.push_back(i);
                ref.push_back(i);
            }
            std::random_shuffle(A.begin(), A.end());
        }

        virtual ~SortingTest() {

        }

        virtual void SetUp() {
            B = A;
        }

        virtual void TearDown() {
            compare();
        }

        void compare() {
            for (int i = 0; i < n; ++i) {
                EXPECT_EQ(B[i], ref[i]);
            }
        }

        int n;
        std::vector<uint32_t> A;
        std::vector<uint32_t> B;
        std::vector<uint32_t> ref;
    };

    TEST_F(SortingTest, insertion_sort) { insertion_sort(B); }
    TEST_F(SortingTest, selection_sort) { selection_sort(B); }
    TEST_F(SortingTest, bubble_sort) { bubble_sort(B); }
    TEST_F(SortingTest, bubble_sort_opt) { bubble_sort_opt(B); }
    TEST_F(SortingTest, hoare_quicksort) { hoare_quicksort(B); }
    TEST_F(SortingTest, lomuto_quicksort) { lomuto_quicksort(B); }
    TEST_F(SortingTest, merge_sort) { merge_sort(B); }
    TEST_F(SortingTest, heapsort) { heapsort(B); }
    TEST_F(SortingTest, radix_sort) { radix_sort(B); }

}  // namespace
