#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Constant: e
'''
Method:
    [e Infinity Limit] [e = (1 + 1/n)ⁿ]
'''
def Limit(i):
    for n in range(1, i):
        print((1.0 + 1.0/n)**n)
