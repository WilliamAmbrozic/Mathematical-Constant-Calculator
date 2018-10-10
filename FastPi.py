#!/usr/bin/env python
# -*- coding: utf-8 -*-
#William Ambrozic 2018
#Make sure you have installed the mpmath package
#Tested in Python2.7
#Not close to chudnovsky just faster than classical methods like eulers formula for pi^2/6

from  mpmath import mp

def givePi(n): #calculatiung pi using newtons method (Newton raphson) on tanx
    pi = 3.1 #starting value
    tmp = 3 #tmp used in order to calculate the next iteration
    mp.dps = n
    while(tmp != pi):
        pi -= mp.tan(pi)
        tmp -= mp.tan(tmp)
    return pi

n = input("# of digits in pi after the decimal?: ")
print(givePi(n))
