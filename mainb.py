import math


def qtd_highprimes(low,high):
    qtd = 0
    for i in range(low,high + 1):
        if is_highprime(i):
            print(i)
            qtd +=1
    return qtd


def is_highprime(n):
    fator = math.sqrt(n)
    if fator % 1 != 0:
        return False
    else:
        return is_prime(int(fator))


def is_prime(fator):
    primes = sieve(fator)
    return primes[fator]



class Sieve():

    def __init__(self, n):
        # Create a boolean array "prime[0..n]" and initialize
        # all entries it as true. A value in prime[i] will
        # finally be false if i is Not a prime, else true.

        self.primes = [True for i in range(n + 1)]
        self.n = n
        p = self.n
        while (p * p <= n):

            # If prime[p] is not changed, then it is a prime
            if (self.prime[p] == True):

                # Update all multiples of p
                for i in range(p * 2, n + 1, p):
                    self.prime[i] = False
            p += 1
        self.prime[0] = False
        self.prime[1] = False

    def get_primes(self, n):
        if n<= self.n:
            return self.primes
        else:
            self.primes += [True for i in range(n,self.n)]
            p = self.n+1




    def sieve(n):
        # Create a boolean array "prime[0..n]" and initialize
        # all entries it as true. A value in prime[i] will
        # finally be false if i is Not a prime, else true.
        prime = [True for i in range(n + 1)]
        p = 2
        while (p * p <= n):

            # If prime[p] is not changed, then it is a prime
            if (prime[p] == True):

                # Update all multiples of p
                for i in range(p * 2, n + 1, p):
                    prime[i] = False
            p += 1
        prime[0] = False
        prime[1] = False

        return prime



# num_casos = int(input())
#
# for _ in range(num_casos):
#     low, high = input().split()
#     low = int(low)
#     high = int(high)
#
#     qtd = qtd_highprimes(low,high)
#     print(qtd)

# while True:
#     n = int(input())
#     print(f"N é primo?: {is_prime(n)}")
#
#     fator = int(math.sqrt(n))
#
#     print (f"Fator: {fator}")
#     print(f"Fator é primo: {is_prime(fator)}")
#     print(f"Fator é high_prime:{is_highprime(n)}")
#
#     primes = known_primes
#
#     for p in range(fator+1):
#         if primes[p]:
#             print(p,end=", ")
