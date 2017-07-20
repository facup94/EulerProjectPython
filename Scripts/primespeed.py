#!/usr/bin/python
import itertools

def erat( ):
    D = {  }
    yield 2
    for q in itertools.islice(itertools.count(3), 0, None, 2):
        p = D.pop(q, None)
        if p is None:
            D[q*q] = q
            yield q
        else:
            x = p + q
            while x in D or not (x&1):
                x += p
            D[x] = p

def main():
    to = int(input('Maximo potential prime: '))
    #f = open('prime_list_up_to_'+str(to)+'.txt', 'w')
    f = open('prueba.txt', 'w')
    try:
        for rees in erat():
            if rees > to:
                break
            f.write(str(rees)+'\n')
    except MemoryError:
        print('got memory error')
        f.close()
    f.close()
        



if __name__ == "__main__":
    main()

