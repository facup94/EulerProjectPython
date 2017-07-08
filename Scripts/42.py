#!/usr/bin/python
import time

triangle_numbers = [0.5*n*(n+1) for n in range(1,400)]

def obtenerValor(palabra):
    suma = 0
    for letra in palabra:
        suma += ord(letra) - 64
    return suma

def main():
    f = open("p042_words.txt",'r')
    t = f.read()
    l = (x[1:-1] for x in t.split(","))

    cant = 0
    for p in l:
        if obtenerValor(p) in triangle_numbers:
            cant += 1

    print(cant,"palabras triangulares")
    
if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
    
