import math

known_primes = [2,3,5]

def is_highprime(n):
    fator = math.sqrt(n)
    if fator % 1 != 0:
        return False
    else:
        return is_prime(fator)


def is_prime(fator):
    fator = int(fator)
    # Corner cases
    if (fator <= 1):
        return False
    if (fator <= 3):
        return True
    if fator < 5:
        return False
    if fator % 5 == 0:
        return False


    for prime in known_primes:
        if prime*prime > fator:
            known_primes.append(fator)
            # print (f'True {prime}, {fator}, {known_primes}')
            return True
        if fator % prime == 0:
            # print(f'False {prime}, {fator}, {known_primes}')
            return False



    i = known_primes[-1] + 6
    # print (f'Prime not known {i}, {fator}, {known_primes}')


    while (i * i <= fator):
        if (fator % i == 0 or fator % (i + 2) == 0):

            return False
        i = i + 6

    known_primes.append(fator)
    return True


def qtd_highprimes(low,high):
    qtd = 0
    for i in range(low,high + 1):
        # print(i)
        if is_highprime(i):
            qtd +=1
    return qtd

num_casos = int(input())

for _ in range(num_casos):
    low, high = input().split()
    low = int(low)
    high = int(high)

    qtd = qtd_highprimes(low,high)
    print(qtd)