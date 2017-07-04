#!/usr/bin/python
import time

def largoRep(cad:[int]) -> int:
    n = cad[-1]
    for i in range(len(cad)):
        if cad[i] == n:
            return (len(cad)-1)-i

def main():
    cadenaMasLarga = 0
    nCadenaMasLarga = 0
    for i in range(2,1000):
        cadena = []
        listadoRestos = []

        entero = 10 // i
        resto = 10%i
        
        cadena.append(entero)
        
        while resto != 0:
            resto *= 10

            entero = resto // i
            resto = resto % i
            
            cadena.append(entero)

            if resto in listadoRestos:
                break

            listadoRestos.append(resto)
           
        largoCadena = largoRep(cadena)
        if largoCadena > cadenaMasLarga:
            cadenaMasLarga = largoCadena
            nCadenaMasLarga = i

        print("i: "+str(i)+" - cadena: 0."+(''.join(str(e) for e in cadena)))

    print("--- / / / / / ----")
    print("d: " + str(nCadenaMasLarga))
    print("largo: " + str(cadenaMasLarga))

        
        

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
    
