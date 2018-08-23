#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy

from .common import *


class MM(APSP):
    # Matrix-multiplication-based
    def main(self):
        self.init_dists()

        tmp_dists = copy.deepcopy(self.dists)
        m = 1
        while m < self.n - 1:
            for i in range(self.n):
                for j in range(self.n):
                    x = float('inf')
                    for k in range(self.n):
                        x = min(x, self.dists[i][k] + self.dists[k][j])
                    tmp_dists[i][j] = x
            self.dists, tmp_dists = tmp_dists, self.dists
            m *= 2


mm = gen_apsp_func(MM)
