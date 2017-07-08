#!/usr/bin/python
import time
from math import sqrt

def triangle_number(number) -> bool:
    c = -2*number
    resolvente = (-1+sqrt(1-4*c))/2
    if resolvente == int(resolvente): return True
    return False

def pentagonal_number(number:int) -> bool:
    c = -2*number
    resolvente = (1+sqrt(1-12*c))/6
    if resolvente == int(resolvente): return True
    return False

def main():
    i = 144
    while True:
        hexagonal = i*(2*i-1)
        if triangle_number(hexagonal) and pentagonal_number(hexagonal):
            print(hexagonal)
            break
        i += 1
    
    
if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
