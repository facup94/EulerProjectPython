#!/usr/bin/python
import time

cubos = []
cubos_permutaciones = {}

def main():
    cubos = [list(str(i**3)) for i in range(10000)]

    for i in range(len(cubos)-1):
        for j in range(i+1, len(cubos)):
            if len(cubos[i]) > len(cubos[j]): break
            if len(cubos[i]) != len(cubos[j]): continue
            dest = cubos[j][:]

            for cifra in cubos[i]:
                if cifra not in dest: break
                dest.remove(cifra)
            if len(dest) == 0:
                if i not in cubos_permutaciones:
                    cubos_permutaciones[i] = set()
                cubos_permutaciones[i].add(j)

                if j not in cubos_permutaciones:
                    cubos_permutaciones[j] = set()
                cubos_permutaciones[j].add(i)
                    
    for key, value in cubos_permutaciones.items():
        if len(value) == 4:
            print(key, "-", value)

        
if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
    
