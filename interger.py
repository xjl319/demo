#!/usr/bin/env python3.4
days = int(input("Enter days:"))
#months = days // 30
#days = days % 30
print("Months = {} Days = {}".format(*divmod(days, 30)))
