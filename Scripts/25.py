#!/usr/bin/python
import time

def fibonacci1(nth:int)-> int:
    if nth < 3: return 1
    return fibonacci(nth-1) + fibonacci(nth-2)

def main():
    n1 = 1
    n2 = 1
    n = 2
    nth = 3
    while(len(str(i)) < 1000):
        n2 = n1
        n1 = n
        n = n1 + n2        
        nth += 1
    print(nth)


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
    
