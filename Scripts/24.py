#!/usr/bin/python
import time

def main():
    cantPermutations = 10*9*8*7*6*5*4*3*2
    print("cantPermutations: "+str(cantPermutations))

    elems = ["0","1","2","3","4","5","6","7","8","9"]

    permutaciones = []
    for a in elems:
        generado = {"0":False,"1":False,"2":False,"3":False,"4":False,"5":False,"6":False,"7":False,"8":False,"9":False}
        generado[a]=True
        for b in [x for x in elems if not generado[x]]:
            generado[b]=True
            for c in [x for x in elems if not generado[x]]:
                generado[c]=True
                for d in [x for x in elems if not generado[x]]:
                    generado[d]=True
                    for e in [x for x in elems if not generado[x]]:
                        generado[e]=True
                        for f in [x for x in elems if not generado[x]]:
                            generado[f]=True
                            for g in [x for x in elems if not generado[x]]:
                                generado[g]=True
                                for h in [x for x in elems if not generado[x]]:
                                    generado[h]=True
                                    for i in [x for x in elems if not generado[x]]:
                                        generado[i]=True
                                        for j in [x for x in elems if not generado[x]]:
                                            generado[j]=True

                                            permutaciones.append([a,b,c,d,e,f,g,h,i,j])

                                            generado[j]=False
                                        generado[i]=False
                                    generado[h]=False
                                generado[g]=False
                            generado[f]=False
                        generado[e]=False
                    generado[d]=False
                generado[c]=False
            generado[b]=False
        generado[a]=False

        
    print(len(permutaciones))
    print(permutaciones[999999])
        
                        
                

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
    
