#!/usr/bin/python
##import sys
##    if len(sys.argv) > 1:
##    maxValue = int(sys.argv[1])

def main():
    flag = True
    n = 20;
    while flag:
        n += 2
        divisiblePorTodos = True
        for i in range(1,21):
            if n % i != 0:
                divisiblePorTodos = False
                break
        if divisiblePorTodos:
            flag = False        
    print(n)

if __name__ == "__main__":
    main()
