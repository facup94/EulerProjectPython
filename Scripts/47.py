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

def separate_in_factors(composite_number:int):
    factors = []
    div2 = composite_number//2
    i = 1
    while composite_number > 1 and i < div2+1:
        i += 1
        if not isPrime(i): continue
        if composite_number % i == 0:
            composite_number = composite_number//i
            factors.append(i)
            i = 1
        
    return sorted(factors)

def group_factors(l):
    salida = []
    while len(l)>0:
        factor = l.pop()
        cant = l.count(factor) + 1
        while l.count(factor) > 0:
            l.remove(factor)
        salida.append(factor**cant)
    return sorted(salida)
    
def shared_numbers(list1, list2, list3, list4):
    shared = []
    for a in list1:
        if a in list2 or a in list3 or a in list4:
            shared.append(a)
    for a in list2:
        if a in list3 or a in list4:
            shared.append(a)
    for a in list3:
        if a in list4:
            shared.append(a)
    return sorted(shared)

def main():
    print(group_factors(separate_in_factors(134043)),group_factors(separate_in_factors(134044)),group_factors(separate_in_factors(134045)),group_factors(separate_in_factors(134046)))
    factorsn3 = [0,1,2,3,4,5,6,7,8,9]
    factorsn2 = [0,1,2,3,4,5,6,7,8,9]
    factorsn1 = [0,1,2,3,4,5,6,7,8,9]
    n = 1
    while True:
        n += 1
        if isPrime(n):
            factorsn3 = [0,1,2,3,4,5,6,7,8,9]
            factorsn2 = [0,1,2,3,4,5,6,7,8,9]
            factorsn1 = [0,1,2,3,4,5,6,7,8,9]
            continue
        factorsn = group_factors(separate_in_factors(n))
        if len(factorsn) != 4:
            factorsn3 = [0,1,2,3,4,5,6,7,8,9]
            factorsn2 = [0,1,2,3,4,5,6,7,8,9]
            factorsn1 = [0,1,2,3,4,5,6,7,8,9]
            continue
        if shared_numbers(factorsn, factorsn1, factorsn2, factorsn3) == []:
            print([i for i in range(n-3,n+1)])
            print([separate_in_factors(i) for i in range(n-3,n+1)])
            print(factorsn3, factorsn2, factorsn1. factorsn)
            break
        factorsn3 = factorsn2
        factorsn2 = factorsn1
        factorsn1 = factorsn
        
    
if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
