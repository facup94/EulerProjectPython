#!/usr/bin/python
import sys

def esPrimo(x : int) -> bool:
    for n in range(x-1,2,-1):
        if x % n == 0:
            return False
    return True

def encontrarPrimerFactor(x:int) -> int:
    for n in range(2, x//2 +1):
        if(x % n == 0) and esPrimo(n):
            return n
    return x

x = 600851475143
if len(sys.argv) > 1:
    x = int(sys.argv[1])

factor = encontrarPrimerFactor(x)
while (factor != x):
    x = x // factor
    factor = encontrarPrimerFactor(x)

print(x)
