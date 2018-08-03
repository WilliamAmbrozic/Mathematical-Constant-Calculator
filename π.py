#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Constant: π
Method:
    [Basel Problem] [(Σ^∞_ₙ₌₁(1/n²)] ↧
    [Euler's Approach] [Σ^∞_ₙ₌₁(1/n²) = π²/6] ↧
    [Implimentation] [π = √[6*[Σ^∞_ₙ₌₁(1/n²)]]]
'''
pi, n = 0.0, 0.0
while (True):
    n+=1
    pi += (1.0/(n*n))
    print ((pi*6)**(0.5))
