#!/usr/bin/python
import time

def wordWorth(cad:str) -> int:
    worth = 0
    for letter in list(cad):
        worth += ord(letter)-64
    return worth

def main():
    file = open(r"C:\Users\Facundo\Desktop\p022_names.txt",'r')
    
    nameList = [x[1:-1] for x in file.read().split(",")]
    nameList.sort()
  
    acum = 0
    for pos in range(len(nameList)):
        acum += (pos+1) * wordWorth(nameList[pos])

    print(acum)

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
    
