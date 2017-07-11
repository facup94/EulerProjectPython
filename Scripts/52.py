#!/usr/bin/python
import time

def main():
    number = 1
    while True:

        digits = sorted(list(str(number)))
        
        flag = True
        for i in range(2,7):
            n = number * i
            ndigits = sorted(list(str(n)))
            if digits != ndigits:
                flag = False
                break
        
        if flag:
            print(number)
            break
        number += 1

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
