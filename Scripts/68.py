#!/usr/bin/python3
import time
from itertools import permutations
from itertools import product

def main():
    maximo = 0
    for perm in permutations([x for x in range(10, 0, -1)]):
        #El primero debe ser el menor de los 5 externos, y un mayor a 6 no dejaria espacio para 4 mas grande
        if perm[0] > 6: continue

        if all(perm[i] != 10 for i in range(1, 5)): continue

        #Ver que lso externos sean mayores que el primer externo
        if any(perm[i] < perm[0] for i in range(1, 5)): continue

        suma = perm[0] + perm[5] + perm[6]

        if suma != perm[1] + perm[6] + perm[7]: continue
        if suma != perm[2] + perm[7] + perm[8]: continue
        if suma != perm[3] + perm[8] + perm[9]: continue
        if suma != perm[4] + perm[9] + perm[5]: continue


        numero = int(''.join([str(perm[i]) for i in [0, 5, 6, 1, 6, 7, 2, 7, 8, 3, 8, 9, 4, 9, 5]]))

        if numero > maximo:
            maximo = numero

    print(maximo)

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
    
