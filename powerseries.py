#!/usr/bin/env python3.4
# -*- coding:utf-8 -*-
# Author: xujl
x = float(input("Enter the value of x: "))
n = term = num = 1
result = 1.0
while n <= 100:
    term *= x / n
    result += term
    n += 1
    if term < 0.0001:
        break

print("No of Times= {} and sum= {}".format(n, result))
