#!/usr/bin/python
import time

def getNextCollatz(n:int) -> int:
    if n%2==0:
        return n//2
    else:
        return 3*n+1

def getCollatz(n:int) -> [int]:
    l = [n]
    while n != 1:
        n = getNextCollatz(n)
        l.append(n)
    return l

def main():
    maxL = 0
    maxNum = 0
    for i in range(1,1000000):
        coll = getCollatz(i)
        if(len(coll) > maxL):
            maxL = len(coll)
            maxNum = i
    print("number:"+str(maxNum)+", len:"+str(maxL))
    

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
    
