from decimal import *

getcontext().prec = 100000

def Factorial(n):
    f = Decimal(1)
    for x in range(1,n+1):
        f *= Decimal(x)
    return f

def main():
    eNewton, eBrother, e, n = Decimal(0.00), Decimal(0.00), "2.", 0
    for n in range(0, getcontext().prec):
        eNewton += (Decimal(1)/Factorial(n))
        eBrother += Decimal(2*n+2)/Factorial(2*n+1)
        try:
            if str(eNewton)[n] == str(eBrother)[n] and n-20 > 0:
                e += str(eNewton)[n-20]
                print(e)
        except IndexError:
            continue
main()
