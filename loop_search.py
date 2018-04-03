# -*- coding: utf-8 -*-
# Assignment 3: Looping, Searching, and Slicing
# Question 1
# Julia Tzu-Ya Weng U07487022

# This program reads numbers input by the user until the user types “done”. 
# Then, it prints out the total, count, maximum, minimum, and average of the 
# entered numbers.

# my own max function
def my_max(items):
    max_item = None
    for item in items:
        if max_item is None or item > max_item:
            max_item = item
    return max_item    
    
# my own min function
def my_min(items):
    min_item = None
    for item in items:
        if min_item is None or item < min_item:
            min_item = item
    return min_item

# my own sum function
def my_sum(items):
    sum_item = 0
    for item in items:
        sum_item += item
    return sum_item

# my own average function
def my_average(items):
    sum_item = 0
    count = 0
    for item in items:
        count += 1
        sum_item += item
    average_item = sum_item/count
    return average_item

# my own append function
def my_append(items, item):
    items += [item]   
    return items
    
# prompt user for input
numbers = []
count = 0
while True:
    try:
        number = raw_input("Enter a number or type \"done\" to finish: ")
        if number.lower() == 'done':
            break
        else:
            my_append(numbers, float(number))
            count += 1
    except:
        print("Enter a valid number or type \"done\" to finish")
 
# if at least a number is enetered    
if count > 0:  
    # print total, count, maximum, minimum and average using my functions
    print("\n\ntotal: %g\n" %my_sum(numbers))
    print("count: %g\n" %count)
    print("maximum: %g\n" %my_max(numbers))
    print("minimum: %g\n" %my_min(numbers))
    print("average: %g\n" %my_average(numbers))
    
#if no numbers are entered, exit
else:
    raise SystemExit("You did not enter any number. Terminating program...")
