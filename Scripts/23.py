#!/usr/bin/python
import time
from math import sqrt

def getSumOfDivisors(n:int) -> int:
    acum = 0
    sqrtn = int(sqrt(n))
    for i in range(1,sqrtn+1):
        if n%i==0:
            acum += i
            acum += (n//i)
    if n == sqrtn * sqrtn: acum -= sqrtn
    acum -= n
    return acum

def isAbundant(n:int)->bool:
    return getSumOfDivisors(n) > n

def armarListaAbundantes(maxN:int)->[int]:
    listOfAbundants = []
    for i in range(1,maxN):
        if isAbundant(i):
            listOfAbundants.append(i)
    return listOfAbundants
   

def main():
    listOfAbundants = armarListaAbundantes(28123)
    print(len(listOfAbundants))
   
    asSumOfAbundants = [False]*28124
    
    for i in range(len(listOfAbundants)-1):
        for j in range(i, len(listOfAbundants)):
            suma = listOfAbundants[i] + listOfAbundants[j]
            if suma > 28123: break
            asSumOfAbundants[suma] = True

    acum = 0
    for i in range(len(asSumOfAbundants)):
        if not asSumOfAbundants[i]:
            acum += i

    print(acum)

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
    
