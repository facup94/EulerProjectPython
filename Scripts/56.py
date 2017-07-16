#!/usr/bin/python
import time

def main():
    max_digital_sum = 0
    for a in range(100):
        for b in range(100):
            numero = a**b
            s_numero = str(numero)
            lista = [int(x) for x  in s_numero]
            sumatoria = sum(lista)
            if sumatoria > max_digital_sum:
                max_digital_sum = sumatoria

    print("Maximum digital sum:", max_digital_sum)

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
