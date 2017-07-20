#!/usr/bin/python
import time
from math import sqrt

def is_triangular(number):
    resolvente = (-1+sqrt(1+8*number))/2
    return resolvente == int(resolvente)

def is_square(number):
    n = sqrt(number)
    return n == int(n)

def is_pentagonal(number):
    resolvente = (1+sqrt(1+24*number))/6
    return resolvente == int(resolvente)

def is_hexagonal(number):
    resolvente = (1+sqrt(1+8*number))/4
    return resolvente == int(resolvente)

def is_heptagonal(number):
    resolvente = (3+sqrt(9+40*number))/10
    return resolvente == int(resolvente)

def is_octogonal(number):
    resolvente = (2+sqrt(4+12*number))/6
    return resolvente == int(resolvente)

def first_two(number):
    n = number
    n /= 100
    return int(n)

def last_two_f2(number, f2):
    n = number
    n -= f2*100
    return int(n)

def last_two(number):
    n = number
    n -= first_two(n)*100
    return int(n)

def main():
    octogonal_list = [i for i in range(1000, 10000) if is_octogonal(i)]
    heptagonal_list = [i for i in range(1000, 10000) if is_heptagonal(i)]
    hexagonal_list = [i for i in range(1000, 10000) if is_hexagonal(i)]
    pentagonal_list = [i for i in range(1000, 10000) if is_pentagonal(i)]
    square_list = [i for i in range(1000, 10000) if is_square(i)]
    triangular_list = [i for i in range(1000, 10000) if is_triangular(i)]

    super_list = [ (7, x) for x in heptagonal_list]
    super_list = super_list + [ (6, x) for x in hexagonal_list]
    super_list = super_list + [ (5, x) for x in pentagonal_list]
    super_list = super_list + [ (4, x) for x in square_list]
    super_list = super_list + [ (3, x) for x in triangular_list]

    for octogonal in octogonal_list:
        f2_1 = first_two(octogonal)
        l2_1 = last_two_f2(octogonal, f2_1)
        cuales_ya_tengo = [8]
        super_list_copy_1 = [ x for x in super_list if first_two(x[1]) == l2_1]
        
        for element1 in super_list_copy_1:
            if element1 == octogonal: continue
            f2_2 = first_two(element1[1])
            l2_2 = last_two_f2(element1[1], f2_2)
            cuales_ya_tengo.append(element1[0])
            super_list_copy_2 = [x for x in super_list if x[0] not in cuales_ya_tengo and first_two(x[1]) == l2_2]

            for element2 in super_list_copy_2:
                if element2 == octogonal or element2 == element1: continue
                f2_3 = first_two(element2[1])
                l2_3 = last_two_f2(element2[1], f2_3)
                cuales_ya_tengo.append(element2[0])
                super_list_copy_3 = [x for x in super_list if x[0] not in cuales_ya_tengo and first_two(x[1]) == l2_3]

                for element3 in super_list_copy_3:
                    if element3 == octogonal or element3 == element2 or element3 == element1: continue
                    f2_4 = first_two(element3[1])
                    l2_4 = last_two_f2(element3[1], f2_4)
                    cuales_ya_tengo.append(element3[0])
                    super_list_copy_4 = [x for x in super_list if x[0] not in cuales_ya_tengo and first_two(x[1]) == l2_4]

                    for element4 in super_list_copy_4:
                        if element4 == octogonal or element4 == element3 or element4 == element2 or element4 == element1: continue
                        f2_5 = first_two(element4[1])
                        l2_5 = last_two_f2(element4[1], f2_5)
                        cuales_ya_tengo.append(element4[0])
                        super_list_copy_5 = [x for x in super_list if x[0] not in cuales_ya_tengo and first_two(x[1]) == l2_5]

                        for element5 in super_list_copy_5:
                            if element5 == octogonal or element5 == element4 or element5 == element3 or element5 == element2 or element5 == element1: continue
                            f2_6 = first_two(element5[1])
                            l2_6 = last_two_f2(element5[1], f2_6)
                            cuales_ya_tengo.append(element5[0])

                            if l2_6 == f2_1:
                                print(8, element1[0], element2[0], element3[0], element4[0], element5[0], sep='\t')
                                print(octogonal, element1[1], element2[1], element3[1], element4[1], element5[1], sep='\t')
                                print(sum([octogonal, element1[1], element2[1], element3[1], element4[1], element5[1]]))

                                #If i found the secuence end all loops
                                cuales_ya_tengo.extend([3,4,5,6,7,8])
                                super_list = []

                            



                            cuales_ya_tengo.remove(element5[0])
                        cuales_ya_tengo.remove(element4[0])
                    cuales_ya_tengo.remove(element3[0])
                cuales_ya_tengo.remove(element2[0])
            cuales_ya_tengo.remove(element1[0])        
                
        
if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))

