#!/usr/bin/python
import time

def isPalindromeBase10(number):
    n = str(number)
    for i in range(len(n)//2):
        if n[i] != n[-(i+1)]: return False
    return True

def isPalindromeBase2(number):
    n = "{0:b}".format(number)
    for i in range(len(n)//2):
        if n[i] != n[-(i+1)]: return False
    return True

def main():
    acum = 0
    for i in range(1,1000000):
        if isPalindromeBase10(i) and isPalindromeBase2(i):
            acum += i
    print("Suma:",acum)
    

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
    
