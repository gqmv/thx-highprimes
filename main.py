import math
import bisect



class HighPrimes():

    def __init__(self, max):
        self.max = max
        self.fator = int(math.sqrt(max))
        self.primes = self.sieve()
        self.high_primesD, self.high_primesL = self.gen_highprimes()


    def sieve(self):
        # Create a boolean array "prime[0..n]" and initialize
        # all entries it as true. A value in prime[i] will
        # finally be false if i is Not a prime, else true.
        prime = [True for i in range(self.fator + 1)]
        p = 2
        while (p * p <= self.fator):

            # If prime[p] is not changed, then it is a prime
            if (prime[p] == True):

                # Update all multiples of p
                for i in range(p * 2, self.fator + 1, p):
                    prime[i] = False
            p += 1
        prime[0] = False
        prime[1] = False

        return prime

    def gen_highprimes(self):
        high_primesD = {}
        high_primesL = []
        qtd = 0
        for i in range(1,self.fator+1):
                if self.primes[i]:
                    i2 = i*i
                    high_primesD[i2] = qtd
                    qtd += 1
                    high_primesL.append(i2)
        return high_primesD, high_primesL

    def qtd(self, low, high):

        try:
            l = self.high_primesD[low]
        except KeyError:
            l = bisect.bisect_right(self.high_primesL, low)

        try:
            h = self.high_primesD[high]+1
        except KeyError:
            h = bisect.bisect_left(self.high_primesL, high)

        return h-l



MAX_DEF = 1000000000000

high = HighPrimes(MAX_DEF)
cases = int(input())
for i in range(cases):
    m, M = input().split()
    print (high.qtd(int(m), int(M)))

