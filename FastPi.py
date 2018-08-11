#!/usr/bin/env python
# -*- coding: utf-8 -*-
#William Ambrozic 2018
#Make sure you have installed the mpmath package
#Tested in Python2.7

from  mpmath import mp

def givePi(n):
    pi = 3.1
    tmp = 3
    mp.dps = n
    while(tmp != pi):
        pi -= mp.tan(pi)
        tmp -= mp.tan(tmp)
    return pi

n = input("# of digits in pi after the decimal?: ")
print(givePi(n))
