#!/usr/bin/env python3.4
# -*- coding:utf-8 -*-
# Author: xujl
n = int(input("Enter the number of rows: "))
num = 0
while num <= n:
    x = ' ' * num
    y = '*' * (n - num)
    print(x+y)
    num += 1
    
