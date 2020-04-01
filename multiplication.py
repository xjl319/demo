#!/usr/bin/env python3.4
# -*- coding:utf-8 -*-
# Author: xujl
i = 1
print("-" * 50)
while i < 11:
    n = 1
    while n <= 10:
        print("{:3d}".format(i * n), end=' ')
        n += 1
    print()
    i += 1
print("-" * 50)
