#!/usr/bin/python
import time
from math import sqrt

list_primes = []
dict_primes = {}

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

def concat(a:int, b:int):
    c = b;
    while c > 0:
        a *= 10;
        c //= 10;
    return a + b;

def check_primality(number):
    global list_primes
    if number > list_primes[-1]:
        return is_prime(number)
    else:
        return number in dict_primes

def fill_primes():
    global list_primes
    global dict_primes
    with open('prime_list.txt','r') as f:
        for line in f:
            number = int(line.strip())
            list_primes.append(number)
            dict_primes[number] = set()

def fill_dictionary(max_index):
    global list_primes
    global dict_primes
    
    for ind_prime1 in range( len(list_primes[:max_index]) - 1 ):
        prime1 = list_primes[ind_prime1]

        for ind_prime2 in range( ind_prime1, len(list_primes[:max_index]) ):
            prime2 = list_primes[ind_prime2]
            
            if check_primality(concat(prime1, prime2)) and check_primality(concat(prime2, prime1)):
                dict_primes[prime1].add(prime2)
                dict_primes[prime2].add(prime1)

def main():
    global list_primes
    global dict_primes
    
    start_time = time.time()
    fill_primes()
    print("--- fill_primes %s seconds ---" % (time.time() - start_time))
    
    max_number = int(input('Maximo prime a concatenar: '))
    max_index = 0
    for prime in list_primes:
        if prime > max_number:
            break
        max_index = max_index + 1
    print("max_index:", max_index)

    start_time = time.time()
    fill_dictionary(max_index)
    print("--- fill_dictionary %s seconds ---" % (time.time() - start_time))

    for element1 in dict_primes:
        if element1 > max_number: continue
        
        for element2 in dict_primes[element1]:
            if element2 > max_number: continue
            
            for element3 in dict_primes[element2]:
                if element3 > max_number: continue
                
                if element1 == element3: continue
                if element1 not in dict_primes[element3]: continue
                if element3 not in dict_primes[element1]: continue

                for element4 in dict_primes[element3]:
                    if element4 > max_number: continue
                    
                    if element1 == element4: continue
                    if element2 == element4: continue
                    if element1 not in dict_primes[element4]: continue
                    if element4 not in dict_primes[element1]: continue
                    if element2 not in dict_primes[element4]: continue
                    if element4 not in dict_primes[element2]: continue

                    for element5 in dict_primes[element4]:
                        if element5 > max_number: continue
                        
                        if element1 == element5: continue
                        if element2 == element5: continue
                        if element3 == element5: continue
                        if element1 not in dict_primes[element5]: continue
                        if element5 not in dict_primes[element1]: continue
                        if element2 not in dict_primes[element5]: continue
                        if element5 not in dict_primes[element2]: continue
                        if element3 not in dict_primes[element5]: continue
                        if element5 not in dict_primes[element3]: continue

                        print(element1, element2, element3, element4, element5, "sum:", sum([element1, element2, element3, element4, element5]))
    

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))

