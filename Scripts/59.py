#!/usr/bin/python
import time
import itertools as it

pruebas = ['about', 'all', 'also', 'and', 'because', 'but', 'can', 'come', 'could', 'day', 'even', 'find', 'first', 'for', 'from', 'get', 'give', 'have', 'her', 'here', 'him', 'his', 'how', 'into', 'its', 'just', 'know', 'like', 'look', 'make', 'man', 'many', 'more', 'new', 'not', 'now', 'one', 'only', 'other', 'our', 'out', 'people', 'say', 'see', 'she', 'some', 'take', 'tell', 'than', 'that', 'the', 'their', 'them', 'then', 'there', 'these', 'they', 'thing', 'think', 'this', 'those', 'time', 'two', 'use', 'very', 'want', 'way', 'well', 'what', 'when', 'which', 'who', 'will', 'with', 'would', 'year', 'you', 'your', 'plain', 'message,', 'bytes', 'impossible', 'The', 'text', 'both', 'without', 'locations,', 'random', 'would', 'made', 'same', 'and', 'key', 'different', 'decrypt', 'the', 'length', 'encrypted', 'user', 'encryption', '"halves",', 'message', 'keep']

def main():
    file = open('p059_cipher.txt','r')
    a = file.read()
    a = a[:-1].split(",")
    cod = [int(x) for x in a]
    passwords = it.permutations([chr(i) for i in range(97,123)], 3)

    for passw in passwords:
        password = [ord(item) for item in list(passw)]*400 + [ord(passw[0])]
        result_ord = [cod_item ^ pass_item for cod_item,pass_item in zip(cod,password)]
        result = [chr(item) for item in result_ord]

        text = ''.join(result)

        cant_found = 0
        for word in pruebas:            
            if word in text:
                cant_found += 1
        if cant_found > 10:
            print(text)
            print("sum:",sum(result_ord))
            break

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))

