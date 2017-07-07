#!/usr/bin/python
import time

def main():
    decimal = ""
    i = 1
    while len(decimal) < 1000000:
        decimal += str(i)
        i += 1
    producto = int(decimal[0]) * int(decimal[9]) * int(decimal[99]) * int(decimal[999]) * int(decimal[9999]) * int(decimal[99999]) * int(decimal[999999])
    print("producto:",producto)
    
    
if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
    
