from math import sqrt
import time

def main():
    maxD = 0
    maxX = 0

    listD = [x for x in range(2, 1001) if int(sqrt(x)) != sqrt(x)]

    print('D', '\t', 'lista', '\t', 'x', '\t', 'y')
    for S in listD:
        mi = 0
        di = 1
        ai = a0 = int(sqrt(S))

        li = [ai]

        while True:
            mi = di * ai - mi
            di = (S - (mi * mi)) // di
            ai = int((a0 + mi) / di)

            li.append(ai)

            numerador = li[-1]
            denominador = 1
            for elem in li[:-1][::-1]:
                numerador, denominador = denominador, numerador
                numerador = denominador * elem + numerador
            print(S, '\t', li, '\t', numerador, '\t', denominador)
            if (numerador ** 2) - S * (denominador ** 2) == 1:
                print(S, '\t', li, '\t', numerador, '\t', denominador)

                if numerador > maxX:
                    maxX = numerador
                    maxD = S
                break

    print(maxD, maxX)


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
