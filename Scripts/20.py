#!/usr/bin/python
import time
from math import factorial

def main():
    fact = factorial(100)
    l = list(str(fact))
    l2 = [int(a) for a in l]
    print(sum(l2))

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
    
