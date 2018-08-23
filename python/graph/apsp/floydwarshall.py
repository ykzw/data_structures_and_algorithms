#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy

from .common import *


class FloydWarshall(APSP):
    def main(self):
        self.init_dists()

        tmp_dists = copy.deepcopy(self.dists)
        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    tmp_dists[i][j] = min(self.dists[i][j],
                                          self.dists[i][k] + self.dists[k][j])
            self.dists, tmp_dists = tmp_dists, self.dists


floyd_warshall = gen_apsp_func(FloydWarshall)
