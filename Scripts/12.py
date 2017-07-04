#!/usr/bin/python
import time
from math import sqrt,ceil

triangles = [1]

def triangle(nth:int) -> int:
    while nth > len(triangles):
        suma =  triangles[-1] + len(triangles) + 1
        triangles.append(suma)
          
    return triangles[nth-1]
    
def cantFactors(x:int) -> int:
    cant = 0
    sqrtx = int(sqrt(x))
    for i in range(1,sqrtx):
        if x%i==0:
            cant+=2

    if x == sqrtx * sqrtx: cant -= 1
    return cant


def main():
    nth = 1
    while(cantFactors(triangle(nth)) <= 500):
        nth += 1
    print(nth)
    print(triangle(nth))
    print(cantFactors(triangle(nth)))
        

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
    
