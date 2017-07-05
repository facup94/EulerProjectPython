#!/usr/bin/python
import time
import itertools

productos = set()
combinaciones = []

def esViable(comb:[str]) -> bool:
    viable = False
    for por in range(1,len(comb)-1):
        for igual in range(por+1,len(comb)):
            elem1 = int(''.join(comb[:por]))
            elem2 = int(''.join(comb[por:igual]))
            prod= int(''.join(comb[igual:]))

            if prod == elem1 * elem2:
                viable = True
                productos.add(prod)
    return viable


def main():
    digitos = ['1','2','3','4','5','6','7','8','9']
    for a in digitos:
        print(a)
        combinacion = [a]
        for b in [x for x in digitos if x not in combinacion]:
            combinacion.append(b)
            for c in [x for x in digitos if x not in combinacion]:
                combinacion.append(c)
                for d in [x for x in digitos if x not in combinacion]:
                    combinacion.append(d)
                    for e in [x for x in digitos if x not in combinacion]:
                        combinacion.append(e)
                        for f in [x for x in digitos if x not in combinacion]:
                            combinacion.append(f)
                            for g in [x for x in digitos if x not in combinacion]:
                                combinacion.append(g)
                                for h in [x for x in digitos if x not in combinacion]:
                                    combinacion.append(h)
                                    for i in [x for x in digitos if x not in combinacion]:
                                        combinacion.append(i)

                                        if esViable(combinacion):
                                            combinaciones.append(combinacion[:])

                                        combinacion.remove(i)
                                    combinacion.remove(h)
                                combinacion.remove(g)
                            combinacion.remove(f)
                        combinacion.remove(e)
                    combinacion.remove(d)
                combinacion.remove(c)
            combinacion.remove(b)

    print(len(combinaciones),"combinaciones")
    print(len(productos),"productos diferentes")
    print("sumatoria:",sum(productos))         

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
    
