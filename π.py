#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Constant: π
from decimal import *
'''
Method:
    [Basel Problem] [(Σ^∞_ₙ₌₁(1/n²)] ↧
    [Euler's Approach] [Σ^∞_ₙ₌₁(1/n²) = π²/6] ↧
    [Implimentation] [π = √[6*[Σ^∞_ₙ₌₁(1/n²)]]]
'''
getcontext().prec = 10000
def Euler():
    pi,n = Decimal(0),0
    while (True):
        n+=1
        pi += (Decimal(1.0/(n*n)))
        print((pi*6)**(Decimal(0.5)))
Euler()
