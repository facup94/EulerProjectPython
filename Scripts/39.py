#!/usr/bin/python
import time
from math import sqrt

p = {}

def main():
    for a in range(1,1000):
        for b in range(a,1000):
            c = sqrt(a**2 + b**2)
            ic = int(c)
            if c != ic: continue
            suma = a + b + ic
            if suma > 1000: break
            if suma in p:
                p[suma] += 1
            else:
                p[suma] = 1
        if b == a: break

    maximo = 0
    pmax = 0
    for key, value in p.items():
        if value > maximo:
            maximo = value
            pmax = key

    print("p:",pmax,"con",maximo,"solutions")
            
            
        
if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
    
