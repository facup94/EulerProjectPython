#!/usr/bin/python
import time

def main():
    pot_max = int(input("->"))
    sumatoria = 0
    for i in range(1, pot_max+1):
        sumatoria += i**i
    print(str(sumatoria)[-10:])

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
    
