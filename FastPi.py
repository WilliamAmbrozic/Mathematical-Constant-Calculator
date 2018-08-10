#!/usr/bin/env python
# -*- coding: utf-8 -*-
#William Ambrozic 2018
from  mpmath import mp
import time

def givePi(n):
    pi = 3.1
    tmp = 3.0
    mp.dps = n
    while(tmp != pi):
        pi -= mp.tan(pi)
        tmp -= mp.tan(tmp)
    return pi

n = input("# of digits in pi after the decimal?: ")
print(givePi(n))
