from math import sqrt

def is_prime(x):
    if x == 1: return False
    if x == 2: return True
    if x%2==0: return False
    if x < 9: return True
    if x%3==0: return False
    
    sqrtx = int(sqrt(x))
    i = 5
    while i <= sqrtx:
        if x % i == 0: return False
        if x % (i+2) == 0: return False
        i=i+6

    return True

with open('prime_list.txt','a') as f:
    i = 171439639
    while i < 200000000:
        if is_prime(i):
            f.write(str(i)+'\n')
        i += 2

print("ENDED i < 200000000")
