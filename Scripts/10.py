#!/usr/bin/python
import time
from math import sqrt

listadoPrimos = []

def esPrimo(x:int) -> bool:
    sqrtx = sqrt(x)
    flag = True
    for i in listadoPrimos:
        if i > sqrtx:
            break
        if x%i==0:
            flag=False
            break
    if flag:
        listadoPrimos.append(x)
    return flag

def main():
    potPrime = 1
    sumatoria = 2
    lim = int(input("Ingrese valor maximo: "))
    while potPrime < lim:
        potPrime += 2
        if(esPrimo(potPrime)):
            sumatoria += potPrime
        
    print(sumatoria)

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
    
