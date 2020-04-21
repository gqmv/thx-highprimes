import math

def qtd_highprimes(low,high, primes, squares):
    qtd = 0
    for i in squares:
        if i >= low and i<=high:
            fator = math.floor(math.sqrt(i))
            qtd += int(primes[fator])
    return qtd

def squares(n):
    sq = []
    i = 1
    inc = 3
    while i<= n:
        sq.append(i)
        i += inc
        inc += 2
    return sq


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

# if __name__ == "__main__":
#
#
#     n = 10000000
#     primes = sieve(math.isqrt(n))
#     squares = squares(n)
#     print (squares)
#     print(qtd_highprimes(1,n,primes, squares))

cases = int(input())
mins = []
maxs = []

for i in range(cases):
    m, M = input().split()
    mins.append(int(m))
    maxs.append(int(M))

n = max(maxs)
fator = math.floor(math.sqrt(n))

primes = sieve(fator)
squares = squares(n)

for m, M in zip(mins, maxs):
    print (qtd_highprimes(m, M, primes, squares))

