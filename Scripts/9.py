#!/usr/bin/python
import time
from math import ceil

def esTriplet(i:int, j:int, k:int) -> bool:
    return (i**2) + (j**2) == (k**2)

def main():
    sumatoria = int(input('Ingrese la sumatoria de a+b+c=>>>>'))
    terminar = False
    for a in range(ceil(sumatoria/3)):
        for b in range(a+1, ceil(((sumatoria-a) /2))):
            c = sumatoria - a - b
            if esTriplet(a,b,c):
                prod = a*b*c

                print("a:"+str(a)+", b:"+str(b)+", c:"+str(c)+", prod:"+str(prod))

                terminar = True
                
            if terminar:
                break
        if terminar:
            break

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
    
