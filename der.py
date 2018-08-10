from  mpmath import mp
import time


pi = 3
mp.dps = 1000000
while(True):
    pi -= mp.tan(pi)
    print(pi)
