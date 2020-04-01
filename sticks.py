#!/usr/bin/env python3.4
# -*- coding:utf-8 -*-
# Author: xujl
import random
sticks = 22

print("There are 21 sticks, you can tak 1-4 number of sticks at a time.")
print("Whoever will take the lask stick will loose")

while sticks > 0:
#while True:
    print("Sticks left: ", sticks)
    if sticks == 1:
        print("You took the last stick, you loose")
        break
    sticks_taken = int(input("Take sticks(1-4):"))
    if sticks_taken >= 5 or sticks_taken <= 0:
        print("Wrong choice")
        continue
    if sticks >= 4:
        a = random.randint(1,4)
    elif sticks < 4:
        a = random.randint(1,sticks - 1)
    print("Computer took: ", a, "\n")
    sticks -= a
