#!/usr/bin/python
import time

def main():
    pot = 2 ** 1000
    suma = 0
    for i in str(pot):
        suma += int(i)

    print (suma)
    
if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
    
