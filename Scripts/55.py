#!/usr/bin/python
import time

def is_palindromic(number):
    snum = str(number)
    mitad = len(snum)//2

    es = True
    for i in range(mitad):
        if snum[i] != snum[-(i+1)]:
            es = False
            break
    return es

def main():
    contador = 0
    for i in range(10,10000):
        a = i
        lychrel = True
        for _ in range(50):
            inverse = int(''.join(reversed(str(a))))
            a = a + inverse
            if is_palindromic(a):
                lychrel = False
                break
        if lychrel:
            contador += 1
    print(contador,"Lychrel numbers under 10.000")

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
