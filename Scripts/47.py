#!/usr/bin/python
import time
from math import sqrt

def separate_in_factors(composite_number:int):
    factors = set()
    sqrtn = int(sqrt(composite_number))
    while composite_number > 1:
        f = find_factor(composite_number)
        factors.add(f)
        composite_number = composite_number // f
    return factors

def find_factor(n) :
    sqrtn = int(sqrt(n))
    for i in range(2, sqrtn + 1) :
        if n % i == 0 :
            return i
    return n

def main():
    contador = 0
    num = 1
    while contador < 4:
        if num%10000==0: print(num//10000)
        if len(separate_in_factors(num)) == 4:
            contador += 1
        else:
            contador = 0
        num += 1

    print("First number:",num-4)
    
if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
