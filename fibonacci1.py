#!/usr/bin/env python3.4
# -*- coding:utf-8 -*-
# Author: xujl
a, b = 0, 1
while b < 100:
    print(b)
    a, b = b, a+b

a, b = 0, 1
while b < 100:
    print(b, end=' ')
    a, b = b, a+b
print()
