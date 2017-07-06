#!/usr/bin/python
import time
import itertools

permutaciones = []
productos = set()

def is_pandigital(n, s=9):
    n=str(n)
    return len(n)==s and not '1234567890'[:s].strip(n)

def producir(perm:[int]):
    viable = True
    elem1 = int(''.join(perm[0]))
    elem2 = int(''.join(perm[1:]))
    prod = elem1 * elem2
    if is_pandigital(str(elem1)+str(elem2)+str(prod)):
        productos.add(prod)
    
    elem1 = int(''.join(perm[:2]))
    elem2 = int(''.join(perm[2:]))
    prod = elem1 * elem2
    if is_pandigital(str(elem1)+str(elem2)+str(prod)):
        productos.add(prod)

def main():
    digitos = ['1','2','3','4','5','6','7','8','9']
    for a in digitos:
        permutacion = [a]
        for b in [x for x in digitos if x not in permutacion]:
            permutacion.append(b)
            for c in [x for x in digitos if x not in permutacion]:
                permutacion.append(c)
                for d in [x for x in digitos if x not in permutacion]:
                    permutacion.append(d)
                    for e in [x for x in digitos if x not in permutacion]:
                        permutacion.append(e)

                        permutaciones.append(permutacion[:])

                        permutacion.remove(e)
                    permutacion.remove(d)
                permutacion.remove(c)
            permutacion.remove(b)
        permutacion.remove(a)

    print(len(permutaciones),"permutacion")
    for e in permutaciones:
        producir(e)

    print("sumatoria",sum(productos))
        
    
if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
    
