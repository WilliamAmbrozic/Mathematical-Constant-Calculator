#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Constant: e
'''
Method:
    [e Infinity Limit] [e = (1 + 1/n)ⁿ]
'''
def Limit(n):
    for x in range(1, n):
        print((1.0 + 1.0/x)**x)
Limit(10)
