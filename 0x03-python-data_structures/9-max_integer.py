#!/usr/bin/python3
def max_integer(my_list=[]):
    max_val = 0
    for x in my_list:
        if x > max_val:
            max_val = x
    return max_val
