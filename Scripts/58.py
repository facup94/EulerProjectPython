#!/usr/bin/python
import time
from math import sqrt

def is_prime(x):
    if x == 1: return False
    if x == 2: return True
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
    ratio = 1
    dist = 2
    last_added = 1
    diagonal_size = 1
    prime_amount = 0
    
    while ratio >= 0.1:
        for _ in range(4):
            last_added += dist
            diagonal_size += 1
            if is_prime(last_added): prime_amount += 1
        dist += 2
        ratio = prime_amount/diagonal_size
    
    print(dist - 1)

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
