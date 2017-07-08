#!/usr/bin/python
import time
import itertools

def main():
    digits = ['0','1','2','3','4','5','6','7','8','9']
    pandigitals = itertools.permutations(digits)

    suma = 0
    for p in pandigitals:
        d234 = int(''.join(p[1:4]))
        if d234 % 2 != 0: continue
        d345 = int(''.join(p[2:5]))
        if d345 % 3 != 0: continue
        d456 = int(''.join(p[3:6]))
        if d456 % 5 != 0: continue
        d567 = int(''.join(p[4:7]))
        if d567 % 7 != 0: continue
        d678 = int(''.join(p[5:8]))
        if d678 % 11 != 0: continue
        d789 = int(''.join(p[6:9]))
        if d789 % 13 != 0: continue
        d8910 = int(''.join(p[7:]))
        if d8910 % 17 != 0: continue

        suma += int(''.join(p))

    print("Suma:",suma)
    
if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
