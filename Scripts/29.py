#!/usr/bin/python
import time

def main():
    l = []
    for a in range(2,101):
        for b in range(2,101):
            l.append(a**b)
    print(len(set(l)))
            

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
    
