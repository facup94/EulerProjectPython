#!/usr/bin/python
import time
from math import sqrt

listadoPrimos = []

def esPrimo(x:int) -> bool:
    if x == 1: return False
    if x < 4: return True
    if x % 2 == 0: return False
    if x < 9: return False
    if x % 3 == 0: return False

    sqrtx = int(sqrt(x))
    i = 5
    while i <= sqrtx:
        if x % i == 0: return False
        if x % (i+2) == 0: return False
        i=i+6

    return True

def main():
    #Formula: n**2 + a*n + b, where |a|<1000 and |b|<=1000

    maxCadena = 0
    nMaxCadena = 0
    
    for a in range(-999, 999):
        print(a)
        for b in range(-1000,1001):
            n=0
            while True:
                pp = n*n + a*n + b
                if pp < 1: break
                if not esPrimo(pp): break
                n += 1

            if n > maxCadena:
                maxCadena = n
                nMaxCadena = a * b

    print(nMaxCadena,"with",maxCadena,"primes")


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
    
