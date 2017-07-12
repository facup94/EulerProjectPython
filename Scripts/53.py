#!/usr/bin/python
import time
from math import factorial

def number_of_combinations(n:int, r:int) -> int:
    fn = factorial(n)
    fr = factorial(r)
    fnr = factorial(n-r)
    return (fn // ( fr * fnr ))

def main():
    contador = 0
    for n in range(23,101):        
        for r in range(1,n+1):
            if number_of_combinations(n,r) > 1000000:
                contador += 1
    print("Cantidad:", contador)


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
