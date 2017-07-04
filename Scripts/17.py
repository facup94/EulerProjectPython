#!/usr/bin/python
import time

predef = {1:"one",2 : "two",3 : "three",4 : "four",5 : "five",
          6:"six", 7:"seven", 8:"eight", 9:"nine",10 : "ten",
          11:"eleven", 12:"twelve", 13:"thirteen", 15:"fifteen", 18:"eighteen",
          20:"twenty", 30 : "thirty", 40:"forty", 50 : "fifty",
          60 : "sixty", 70:"seventy", 80:"eighty", 90:"ninety",
          1000:"one thousand"}
          
def convertToString(n:int) -> str:
    if n in predef:
        return predef[n]

    cadena = ""
    if n > 99:
        cadena += predef[n//100]
        cadena += " hundred"
        if(n%100==0):
            return cadena
        cadena += " and "

    resto = n%100

    if resto in predef:
            cadena += predef[resto]
            return cadena
    
    if resto < 20:        
        cadena += predef[resto%10]
        cadena += "teen"
        return cadena

    cadena += predef[(resto//10) * 10]
    cadena += "-"
    cadena += predef[resto%10]
    return cadena


def main():
    strCount = 0
    for number in range(1,1001):
        strCount += len(convertToString(number).replace(" ","").replace("-",""))
    print(strCount)           
    
    
if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
    
