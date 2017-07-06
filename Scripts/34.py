#!/usr/bin/python
import time
import itertools as it
from math import factorial

##def valid(comb):
##    if comb == (0,0,1) or comb == (0,0,2): return False
##    acum = 0
##    if comb[0] == 0: acum -= 1
##    for e in comb:
##        acum += factorial(e)
##    if acum == int(''.join([str(x) for x in comb])): return True
##    return False

def valid(comb):
    acum = 0
    for e in str(comb):
        acum += factorial(int(e))
    if acum == comb: return True
    return False
    
def main():
    acum = 0
    c = 3
    for i in range(9999999):
        if valid(c):
            acum += c
        c += 1
    print("sumatoria:",acum)
    
if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
    
