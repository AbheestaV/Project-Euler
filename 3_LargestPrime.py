#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 16:46:23 2023

@author: zod


The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""

n = 600851475143
c = 2

while n > 1:
    if n % c == 0:
        n = n/c
        max = c
    else:
        c = c+1

print(max)