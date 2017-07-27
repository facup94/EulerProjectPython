#!/usr/bin/python
def main():
    maxN = 1000
    #input
    sumatoria = 0
    for i in range(maxN):
        if (i % 3 == 0) or (i % 5 == 0):
            sumatoria += i
    print(sumatoria)

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
    
