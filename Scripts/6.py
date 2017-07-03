#!/usr/bin/python
##import sys
##    if len(sys.argv) > 1:
##    maxValue = int(sys.argv[1])

def main():
    sumOfSquares = 0
    squareOfSum = 0

    for i in range(1,101):
        sumOfSquares += i * i

    squareOfSum = ((100+1)*(100//2)) ** 2
    
    dif = squareOfSum - sumOfSquares
    print(dif)


if __name__ == "__main__":
    main()
