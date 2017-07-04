#!/usr/bin/python
import time

##diasXMes = {"enero":31,"febrero":28,"marzo":31,"abril":30,"mayo":31,"junio":30,
##            "julio":31,"agosto":31,"septiembre":30,"octubre":31,"noviembre":30,"diciembre":31}
nombreMes = {1:"enero",2:"febrero",3:"marzo",4:"abril",5:"mayo",6:"junio",
            7:"julio",8:"agosto",9:"septiembre",10:"octubre",11:"noviembre",12:"diciembre"}
diasXMes = {1:31,2:28,3:31,4:30,5:31,6:30,
            7:31,8:31,9:30,10:31,11:30,12:31}


def main():
    day = 0
    cantDom = 0
    for anio in range(1900,2001):
        leapYear = (anio%4==0 and anio%100!=0) or anio%400==0
        for mes in range(1,13):
            cantDias = diasXMes[mes]+1
            if mes==2 and leapYear:
                cantDias += 1
            for dia in range(1,cantDias):
                day += 1
                if day==7:
                    day=0
                    if(dia==1 and anio != 1900):
                        cantDom += 1
                        print("Domingo: primero de "+str(nombreMes[mes])+" de "+str(anio))

    print(cantDom)
    
if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
    
