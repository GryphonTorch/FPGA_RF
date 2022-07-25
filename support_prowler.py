#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 01:22:22 2022

@author: yujun
"""
import numpy as np

bitValues = [1,1,3, 4,5,5, 7,8,9, 10]
sampling = 3


def flip_counter(full_list, sampling):
    """
    Function to down-sample full_list (high frequency signal of 0 and 1s)
    into chunks of width sampling, and counts the number of 0->1 or 1->0
    transitions within each chunk. 
    Returns two lists of "time" and flip count values (for ease of plotting)  
    """
    total_flips = []   # initialize history list
    counter = []       # for [1,2,3...]
    
    work_list = full_list[0:(len(full_list) // sampling)*sampling]
    # discard last few bits
    
    count = 0
    
    for idx in range(len(work_list)):
        flip = 0
        if np.mod(idx, sampling)  == 0:     
            for idx2 in range(idx, idx+sampling-1):
                if work_list[idx2+1] != work_list[idx2]:
                    flip += 1
            total_flips.append(flip)
            count += 1
            counter.append(count)
     
    return counter, total_flips
    
test_counter, test_flips = flip_counter(bitValues, sampling)
print("test_counter, test_flips:", test_counter, test_flips)