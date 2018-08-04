#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Constant: φ
'''
Method:
    [Fibonacci Converging Quotients] [φ = limₙ→∞(Fₙ₊₁/Fₙ)]
'''
def FCQ():
    fnplus1,fn,tmp = 1,1,0
    while (True):
        fn = fnplus1
        fnplus1 = tmp
        tmp = fn + tmp
        if fn != 0:
            print(float(fnplus1/fn))
