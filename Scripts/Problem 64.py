#!/usr/bin/python
import time
import math

def main():
    contador = 0
    for number in range(2,10001):
        valores = []
        
        mi = 0
        di = 1
        ai = math.floor(math.sqrt(number))

        while True:
            
            mi_1 = di*ai - mi

            di_1 = (number-(mi_1**2))//di
            if di_1==0:
                break
            ai_1 = (math.floor(math.sqrt(number))+mi_1)//di_1

            if (mi_1,di_1,ai_1) in valores:
                break

            valores.append((mi_1,di_1,ai_1))
            mi = mi_1
            di = di_1
            ai = ai_1

        if len(valores)%2!=0:
            contador += 1

    print(contador)
        
if __name__ == "__main__":
    start_time = time.time()
    main()
print("--- %s seconds ---" % (time.time() - start_time))
