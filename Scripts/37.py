#!/usr/bin/python
import time
from math import sqrt

def isPrime(x:int) -> bool:
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

def isTruncatable(num):
    if not isPrime(num): return False
    n = str(num)
    for x in range(1, len(n)):
        if not isPrime(int(n[x:])): return False
        if not isPrime(int(n[:x])): return False
    return True
    

def main():
    acum = 0
    i = 11
    truncatables = []
    while len(truncatables) < 11:
        if isTruncatable(i):
            truncatables.append(i)
        i += 1
    print("Suma:",sum(truncatables))

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
    
