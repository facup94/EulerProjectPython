#!/usr/bin/python
import sys

def main():
    maxPalindromo = 0
    for i in range(999,1,-1):
        for j in range(999,1,-1):
            numero = i * j
            if(palindromo(str(numero)) and numero>maxPalindromo):
                maxPalindromo = numero
    print(maxPalindromo)

def palindromo(x:str) -> bool:
    pal = True
    for i in range(0, len(x) //2):
        if(x[i] != x[-(1+i)]):
            pal = False
            break
    return pal

if __name__ == "__main__":
    main()
