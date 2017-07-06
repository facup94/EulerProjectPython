#!/usr/bin/python
import time
from functools import reduce # Valid in Python 2.6+, required in Python 3
import operator

fracciones = []

def reducir(n, d, res):
    a = tuple(str(x) for x in [n,d])
    for d in [str(x) for x in range(1,10)]:
        if d not in a[0] or d not in a[1]: continue
        
        b = tuple(_.replace(d,"",1) for _ in a)
        if not b[0] or b[0].startswith("0"): continue
        if not b[1] or b[1].startswith("0"): continue

        return res == int(b[0])/int(b[1])
    return False

def separarEnPrimos(num):
    s = []
    i = 1
    while num > 1:
        i += 1
        if num%i==0:
            s.append(i)
            num /= i
            i = 1
    return s
    
def main():
    numerador = 10
    denominador = 10
    while(len(fracciones) < 4):
        if numerador > 99 or denominador > 99: break
        
        division = numerador / denominador
        if division >= 1:
            numerador = 10
            denominador += 1
            continue

        if reducir(numerador, denominador, division):
            fracciones.append((numerador,denominador))
        
        numerador += 1

    print("fracciones",fracciones)

    for i in range(len(fracciones)):
        x = [separarEnPrimos(fracciones[i][0]),separarEnPrimos(fracciones[i][1])]
        fracciones[i] = x

    print("separadas en primos:",fracciones)

    superNumerador = [elemento for numerador in [fraccion[0] for fraccion in fracciones] for elemento in numerador]
    superDenominador = [elemento for denominador in [fraccion[1] for fraccion in fracciones] for elemento in denominador]
    print("superNumerador:",superNumerador)
    print("superDenominador:",superDenominador)

    for a in superNumerador[:]:
        if a in superDenominador:
            superNumerador.remove(a)
            superDenominador.remove(a)

    superNumerador.append(1)
    superDenominador.append(1)
    print("superNumerador:",superNumerador)
    print("superDenominador:",superDenominador)

    numerador = reduce(operator.mul, superNumerador, 1)
    denominador = reduce(operator.mul, superDenominador, 1)
    print("numerador:",numerador)
    print("denominador:",denominador)
    
if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
    
