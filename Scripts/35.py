#!/usr/bin/python
import time
from math import sqrt

def esPrimo(x:int) -> bool:
    if x == 1: return False
    if x < 4: return True
    if x % 2 == 0: return False
    if x < 9: return True
    if x % 3 == 0: return False

    sqrtx = int(sqrt(x))
    i = 5
    while i <= sqrtx:
        if x % i == 0: return False
        if x % (i+2) == 0: return False
        i=i+6

    return True

def isCircular(numero):
    n = str(numero)
    for i in range(len(n)):
        if not esPrimo(int(n)): return False
        n = n[-1] + n[:-1]
    return True

def main():
    cantidad = 0
    for i in range(2,1000000):
        if isCircular(i):
            cantidad += 1
    print("cantidad:",cantidad)

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
    
