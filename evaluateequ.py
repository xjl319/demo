#!/usr/bin/env python3.4
# -*- coding:utf-8 -*-
# Author: xujl
sum = 0
N = 100
for i in range(1,N+1):
    sum += 1.0 / i
    print("{:2d} {:6.4f}".format(i, sum))
