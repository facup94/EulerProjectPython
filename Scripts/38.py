#!/usr/bin/python
import time

digits = ["1","2","3","4","5","6","7","8","9"]
largestPan = 0
largestPanProducer = ()

def pandigital(num, n):
    global largestPan, largestPanProducer
    productos = []
    for x in range(1,n+1):
        prod = list(str(num*x))
        if len(prod) > 9: return 2
        productos.extend(prod)
        if len(productos) > 9: return 1
    if len(productos) != 9: return -2
    if sorted(productos) == digits:
        if int(''.join(productos)) > largestPan:
            largestPan = int(''.join(productos))
            largestPanProducer = (num, n)
        return 0
    return -1

def main():
    j = 2
    i=0
    while i < 10000:
        res = pandigital(i,j)
       
        if res > 0:
            j += 1
            print("j:",j,"->i:",i)
            i=0

        if res == 0:
            print("[PANDIGITAL] i:",i,"j:",j,"res:",res)

        if i == 9999:
            j+= 1
            print("j:",j,"->i:",i)
            i=0

        if j == 9:
            print("[BREAK] j:",j,"->i:",i)
            break

        i += 1

    print("Result:",largestPan)
    print("Produced by:",largestPanProducer)
        
if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
    
