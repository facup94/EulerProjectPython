#!/usr/bin/python
import time
from math import sqrt

cantLlamadas = 0

def sumOfProperDiv(n:int) -> int:
    global cantLlamadas
    cantLlamadas += 1
    suma = 1
    sqrtn = int(sqrt(n))
    for i in range(2,sqrtn+1):
        if n%i==0:
            suma += i
            suma += (n//i)
    if n == sqrtn * sqrtn: suma -= sqrtn
    return suma
        

def main():
    acum = 0
    for i in range(1,10000):
        v = sumOfProperDiv(i)
        if i == v: continue
        if v>i and i == sumOfProperDiv(v):
            acum += i+v
    print(acum)
    global cantLlamadas
    print(cantLlamadas)

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
    
