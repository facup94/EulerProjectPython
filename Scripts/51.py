#!/usr/bin/python
import time
from math import sqrt
import itertools as it

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
    fill_primes(int(input('max number ->')))

    for prime in primes:
        flag = False
        list_prime = list(str(prime))
        set_prime = set(list_prime)

        for num in set_prime:
            cantidad = 0
            for i in ['0','1','2','3','4','5','6','7','8','9']:
                if i=='0' and num == list_prime[0]: continue
                list_prime_copy = [x if x != num else i for x in list_prime]
                if is_prime(int(''.join(list_prime_copy))):
                    cantidad += 1
            if cantidad == 8:
                print(prime,"swapping number",num,"for other digits")
                flag = True
                break
        if flag: break

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
