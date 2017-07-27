#!/usr/bin/python
import time

def main():
    cant = 0
    for b in range(1, 1001):
        for a in range(1,10):
            if len(str(a**b)) == b:
                cant += 1
    print(cant)
        
if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
    
