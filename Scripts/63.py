#!/usr/bin/python
import time

def main():
    cant = 0
    for a in range(1, 10): #Esto se puede reducir ya que para a>=10 len(a**b)>b
        b = 1
        potL = len(str(a**b))
        while potL == b:
            cant += 1
            b += 1
            potL = len(str(a**b))

    print(cant)
        
if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
    
