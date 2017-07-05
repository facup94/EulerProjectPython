#!/usr/bin/python
import time

def main():
    combinaciones = ["2L: 1"]
    for monedas1L in range(0,3):
        restante = 200

        combinacion={"1L":monedas1L}
        restante -= monedas1L * 100

        for monedas50p in range((restante//50)+1):
            combinacion["50p"]=monedas50p
            restante -= monedas50p * 50

            for monedas20p in range((restante//20)+1):
                combinacion["20p"]=monedas20p
                restante -= monedas20p * 20

                for monedas10p in range((restante//10)+1):
                    combinacion["10p"]=monedas10p
                    restante -= monedas10p * 10

                    for monedas5p in range((restante//5)+1):
                        combinacion["5p"]=monedas5p
                        restante -= monedas5p * 5

                        for monedas2p in range((restante//2)+1):
                            combinacion["2p"]=monedas2p
                            restante -= monedas2p * 2

                            monedas1p = restante
                            combinacion["1p"]=monedas1p

                            combinaciones.append(list(combinacion.values()))

                            restante += monedas2p * 2
                        restante += monedas5p * 5
                    restante += monedas10p * 10
                restante += monedas20p * 20
            restante += monedas50p * 50
        restante += monedas1L * 100

##    for elem in combinaciones:
##        print(elem)
    print(str(len(combinaciones)),"combinaciones")    

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
    
