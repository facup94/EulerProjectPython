#!/usr/bin/python
import time

collatz = {1:[1]}

def getNextCollatz(n:int) -> int:
    if n%2==0:
        return n//2
    else:
        return 3*n+1

def getCollatz(n:int) -> [int]:
    if n in collatz:
        return collatz[n]
    x = n
    l = []
    while x not in collatz:
        l.append(x)
        x = getNextCollatz(x)
        if x == 1: break

    l.extend(collatz[x])
    collatz[n] = l
    return l
    

def main():
    maxLen = 0
    maxN = 0
    for i in range(1,1000000):
        l = len(getCollatz(i))
        if l > maxLen:
            maxLen = l
            maxN = i
    
    print(maxN)

    

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
    
