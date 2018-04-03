# -*- coding: utf-8 -*-
# Assignment 3: Looping, Searching, and Slicing
# Question 2
# Julia Tzu-Ya Weng U07487022

# This program extract a number from a string

avg_str = 'Average value read: 0.72903'

# get position for colon
colon_pos = avg_str.find(':') 

# extract number
number = avg_str[colon_pos + 1:]

# strip white space, if any
number = number.strip()

#convert number to float
number = float(number)

# print number
print number
