#!/usr/bin/python
import time

cubos = []
cubos_permutaciones = {}

def mi_resp_original():
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


def main():
    cubes = []
    i = 1

    while True:
        cube = sorted(list(str(i**3)))

        cubes.append(cube)

        if cubes.count(cube) == 5:
            print("permutacion",cube)
            ind = -1
            print("valores que producen permutaciones: [", end='')
            for j in range(5):
                ind = cubes.index(cube, ind+1)
                print(ind, end=', ')
            print("]")
            print("minimo cubo", cubes.index(cube) ** 3)
            break
        i += 1

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
    
