#!/usr/bin/python
import time
import itertools
from math import sqrt

def isPrime(x):
    if x == 1: return False
    if x < 3: return True
    if x%2==0: return False
    if x < 9: return True
    if x%3==0: return False
    
    sqrtx = int(sqrt(x))
    i = 5
    while i <= sqrtx:
        if x % i == 0: return False
        if x % (i+2) == 0: return False
        i=i+6

    return True

def main():
    digitos = ['1','2','3','4','5','6','7','8','9']
    for ndigital in range(9,0,-1):
        perm = itertools.permutations(digitos[:ndigital])
        lperm = list(perm)
        lperm.reverse()
        for t in lperm:
            if isPrime(int(''.join(t))):
                print(int(''.join(t)))
                break
    
if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
    
