#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 16:13:25 2022
synth_system.bit
or use bitstream

@author: yujun
Numpy fromfile documentation:
    https://numpy.org/doc/stable/reference/generated/numpy.fromfile.html
"""

# https://stackoverflow.com/questions/5552555/unicodedecodeerror-invalid-continuation-byte 
# I googled the error message and suppose the encoding is latin-1 ?

f = open('synth_system.bit')
print(f)
f.read(1)

