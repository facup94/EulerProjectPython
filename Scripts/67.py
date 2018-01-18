#!/usr/bin/python3
import time
from math import sqrt

def main():
    triangulo = []

    #Leo el archivo y lo cargo en una lista de listas
    with open('p067_triangle.txt', 'r') as file:
        for linea in file:
            triangulo.append(linea[:-1].split(' '))

    #Convierto cada elemento del triangulo en entero
    for i in range(len(triangulo)):
        for j in range(len(triangulo[i])):
            triangulo[i][j] = int(triangulo[i][j])

    #A cada linea despues de la cuspide
    for linea in range(1,len(triangulo)):
        #Al primer elemento de la lionea le sumo el primer elemento de la linea superior
        triangulo[linea][0] += triangulo[linea-1][0]
        #Al ultimo elemento de la lionea le sumo el ultimo elemento de la linea superior
        triangulo[linea][-1] += triangulo[linea - 1][-1]

        #Para el resto le sumo el mayor de los dos posibles "padres" (izquierdo o derecho)
        for col in range(1, len(triangulo[linea])-1):
            triangulo[linea][col] += triangulo[linea-1][col-1] if triangulo[linea-1][col-1]>triangulo[linea-1][col] else triangulo[linea-1][col]

    #Reviso cual es el maximo de los elementos de la base de la piramide
    sumaMax = 0
    for elem in triangulo[-1]:
        if elem > sumaMax:
            sumaMax = elem
    print(sumaMax)


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
    
