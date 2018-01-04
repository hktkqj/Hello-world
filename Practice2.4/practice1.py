#!/usr/bin/python
# -*- coding: UTF-8 -*-
hours = input("Please input hours\n")
hours = int(hours)
second_per_hour=60*60
print(str(hours) + " hours equals " + str(second_per_hour*hours) + " seconds.")
second_per_day=24*second_per_hour
print(second_per_day/second_per_hour)
print(second_per_day//second_per_hour)
