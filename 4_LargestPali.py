#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 16:53:23 2023

@author: zod


A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""

def isPal():
    max = 1
    for i in range(999, 100, -1):
        for j in range (999, 100, -1):
            if str(i*j) == str(i*j)[::-1]:
                if (i*j)>max:
                    max = i*j
    return max
                
def main():
    print(isPal())
    
if __name__ == "__main__":
    main()
    


