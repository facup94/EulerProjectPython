#!/usr/bin/python
import time

def main():
    M = N = int(input("Size:"))
    mat = [ [0]*(M+1) for _ in range(N+1) ]
    
    for i in range(M,-1,-1):
        for j in range(N,-1,-1):
            cantOp = 0
            if i != M:
                cantOp += mat[i+1][j]
            if j != N:
                cantOp += mat[i][j+1]
            if i == M and j==N:
                cantOp = 1
                
            mat[i][j] = cantOp

    print(mat)
    
if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
    
