#!/usr/bin/python
import time

def main():
    numerador = 1
    denominador = 1
    cant = 0
    for i in range(1000):
        numerador += denominador
        numerador, denominador = denominador, numerador
        numerador += denominador

        if (len(str(numerador)) > len(str(denominador))):
            cant += 1

    print("Cantidad:", cant)
    

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
