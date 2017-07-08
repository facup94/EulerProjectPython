#!/usr/bin/python
import time
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

def can_be_written_as(number:int) -> bool:
    for prime in range(number-1,1,-1):
        if not isPrime(prime): continue
        x = sqrt((number-prime)/2)
        if x == int(x): return False
    return True

def main():
    i = 33
    while True:
        i += 2
        if isPrime(i): continue
        if can_be_written_as(i):
            print(i)
            break

        
    
if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
