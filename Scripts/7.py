#!/usr/bin/python
import time
from math import sqrt
##import sys
##    if len(sys.argv) > 1:
##    maxValue = int(sys.argv[1])

listadoPrimos = []

def esPrimo(x:int) -> bool:
    primo = True
    sqrtx = sqrt(x)
    for i in listadoPrimos:
        if i > sqrtx:
            break
        if x%i == 0:
            primo = False
            break
    if primo:
        listadoPrimos.append(x)
    return primo

def main():
    contador = 1
    numero = 1
    while contador < 10001:
        numero += 2
        if esPrimo(numero):
            contador += 1

    print(numero)


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
    
