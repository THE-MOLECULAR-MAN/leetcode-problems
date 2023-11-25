#!/usr/bin/python3
# /usr/bin/python3 -m pip install numpy
import numpy as np

def is_descending(r) -> bool:
    # print('sorted version: ', sorted(r))
    return r == sorted(r, reverse=True)

def get_subtraction_list(l):
    """x"""

def find_next_change(l):
    """x"""
    for i in l:
        if 

def romanToInt(s: str):
    mapping={'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }
    print('-------------------------')
    print('original: ', s)

    # if len(s) == 0:
    #     return 0
    # elif len(s) == 1:
    #     return mapping[s[0]]
    
    # while iter<len(s)-1:
    #     x=mapping[s[iter]]
    #     x_next=mapping[s[iter+1]]
    #     if x_next > x:
    #         # need to do subtraction


    # romans_as_array = [char for char in s]
    numerical_list=[]
    for c in s:
        numerical_list.append(mapping[c])

    if is_descending(numerical_list):
        print('no logic needed, list is descending')
        return sum(numerical_list)

    print('gotta do some logic, it is ascending')
    
    return numerical_list

print(romanToInt('I'))
print(romanToInt(''))
print(romanToInt('III'))
print(romanToInt('IV'))
print(romanToInt('VI'))