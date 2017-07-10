#!/usr/bin/python
import time
import itertools as it
from math import sqrt

def is_prime(n):
    if n == 1: return False
    if n == 2: return True
    if n % 2 == 0: return False
    if n < 9: return True
    if n % 3 == 0: return False
    
    sqrtn = int(sqrt(n))
    i = 5
    while i <= sqrtn:
        if n % i == 0: return False
        if n % (i+2) == 0: return False
        i=i+6

    return True

def main():
    originales_con_primos = []
    for i in range(1000, 10000):
        if not is_prime(i): continue
        if i == 1487: continue
        
        permutations_of_i = it.permutations(str(i))
        primos = []

        for permutation in permutations_of_i:
            pot_prime = int(''.join(permutation))
            if pot_prime not in primos and is_prime(pot_prime):
                primos.append(pot_prime)

        primos = [x for x in primos if x>=primos[0]]
        primos.sort()
        
        if len(primos) < 3: continue

        originales_con_primos.append([primos, [x-primos[0] for x in primos]])


    final_elements = []
    for element in originales_con_primos:
        temp = [[element[0][0]],[element[1][0]]]
        for i in range(1,len(element[1])):
            if element[1][i]*2 in element[1] or element[1][i]//2 in element[1]:
                temp[0].append(element[0][i])
                temp[1].append(element[1][i])
        if len(temp[0]) > 2:
            final_elements.append(temp)

    for a in final_elements:
        print(''.join([str(x) for x in a[0]]))
        print(a[0])
        print(a[1])
        print()
        
        
        

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
