#!/usr/bin/python
import time
from math import sqrt

primes = [2]

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

def fill_primes(maximum):
    for i in range(1,maximum,2):
        if is_prime(i): primes.append(i)
    

def main():
    fill_primes(1000000)

    max_prime_as_sum = 0
    amount_of_consecutives = 0
    s = 0
    e = 0
    for start in range(len(primes)-1):
        for end in range(start+1,len(primes)+1):
            as_sum = sum(primes[start:end])
            if as_sum < 1000: continue
            if as_sum > 1000000: break
            if not is_prime(as_sum): continue

            cant = end-start
            if cant > amount_of_consecutives:
                amount_of_consecutives = cant
                max_prime_as_sum = as_sum
                s = start
                e = end

    print("Max prime:",max_prime_as_sum,"can be expresed as a sum of",amount_of_consecutives,"primes (from",s,"to",e,")")
            
        

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
