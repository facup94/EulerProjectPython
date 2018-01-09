#!/usr/bin/python3
import time

def main():
    continuedFraction = [2]
    for i in range(1,35):
        continuedFraction.extend([1, 2*i, 1])

    continuedFraction = continuedFraction[:100]

    numerador = continuedFraction[99]
    denominador = 1
    for j in continuedFraction[:99][::-1]:
        aux = denominador
        denominador = numerador
        numerador = j * denominador + aux
    print(numerador, '/', denominador)
    print('Suma de digitos:', sum([int(x) for x in list(str(numerador))]))
    
    
if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
