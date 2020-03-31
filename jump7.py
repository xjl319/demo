#!/usr/bin/env python3.4
# -*- coding:utf-8 -*-
# Author: xujl
print('''逢7跳过''')
for i in range(101):
    if '7' in str(i) or i % 7 == 0:
        continue
    print(i)

for i in range(101):
    if i % 7 == 0 or i // 10 == 7 or i % 10 == 7:
        continue
    print(i)

