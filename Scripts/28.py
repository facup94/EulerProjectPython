#!/usr/bin/python
import time

def imprimirMatriz(mat):
    cadena = ""
    for fila in mat:
        for elemento in fila:
            cadena += str(elemento)+"\t"
        cadena += "\n"
    print(cadena)

def main():
    size = int(input("SIZE:"))
    mat = [[0]*size for x in range(size)]

    fila = columna = int(size/2)
    contador = 1
    repetidor = 1
    mat[fila][columna] = contador

    while True:
        if repetidor%2==0:
            for i in range(1, repetidor+1):
                contador += 1
                columna -= 1 if columna>0 else 0
                mat[fila][columna] = contador
            for i in range(1, repetidor+1):
                contador += 1
                fila -= 1 if fila>0 else 0
                mat[fila][columna] = contador
        else:
            for i in range(1, repetidor+1):
                contador += 1
                if columna<(size-1):
                    columna += 1
                else: break
                mat[fila][columna] = contador
            if mat[0][-1]!= 0:
                break
            for i in range(1, repetidor+1):
                contador += 1
                fila += 1 if fila<(size-1) else 0
                mat[fila][columna] = contador

        repetidor += 1
        
    acumulador = 0
    for i in range(size):
        acumulador += mat[i][i]
        acumulador += mat[i][-(i+1)]
    acumulador -= 1
    print(acumulador)
        

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
    
