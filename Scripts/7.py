#!/usr/bin/python
import time
from math import sqrt
##import sys
##    if len(sys.argv) > 1:
##    maxValue = int(sys.argv[1])

listadoPrimos = []

def esPrimo(x:int) -> bool:
    if x == 1: return False
    if x < 4: return True
    if x % 2 == 0: return False
    if x < 9: return False
    if x % 3 == 0: return False

    sqrtx = int(sqrt(x))
    i = 5
    while i <= sqrtx:
        if x % i == 0: return False
        if x % (i+2) == 0: return False
        i=i+6

    return True

def generarListadoPrimos(cantidad:int):
    listadoPrimos.extend([2, 3, 5, 7])
    candidato = 9
    while len(listadoPrimos) < cantidad:
        candidato += 2
        if esPrimo(candidato):
            listadoPrimos.append(candidato)

    print("Listado Primos generado")
            
def main():
    generarListadoPrimos(10001)

    print(listadoPrimos[-1])


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
    
