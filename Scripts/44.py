#!/usr/bin/python
import time

p = [n*(3*n-1)/2 for n in range(1,10001)]
pentagonal_numbers = dict(zip(p,p))

def main():
    minSetted = False
    minim = -1
    for i in pentagonal_numbers:
        for j in pentagonal_numbers:
            resta = i - j
            D = abs(resta)

            if D > minim and minSetted: continue

            if resta not in pentagonal_numbers: continue
            
            suma = i + j
            if suma not in pentagonal_numbers: continue
            
            minim = D
            minSetted = True

    print("Minim D:",minim)
    
if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
