#!/usr/bin/python
import time
from math import sqrt

def main():
    contador = 0
    for number in range(2, 10001):
        cantValores = 0
        
        m = 0
        d = 1
        a = int(sqrt(number))
        a0 = int(sqrt(number))

        if a0 == sqrt(number):
            continue

        while a != 2*a0:
            
            m = d*a - m

            d = (number-(m**2))//d
            if d == 0:
                break
            a = (a0+m)//d
            cantValores += 1

        if cantValores % 2 != 0:
            contador += 1
    print(contador)
        
if __name__ == "__main__":
    start_time = time.time()
    main()
print("--- %s seconds ---" % (time.time() - start_time))
