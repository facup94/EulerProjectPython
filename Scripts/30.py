#!/usr/bin/python
import time

def main():
    cantNumeros = int(input("Cant Numeros: "))
    numeros = []
    n = 2
    nTime = time.time()
    while True:
        suma = sum([int(x)**5 for x in list(str(n))])
        if n == suma:
            numeros.append(n)
            nTime = time.time()

        n += 1

        if time.time() - nTime > 60:
            break
    print(numeros)
    print(sum(numeros))

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
    
