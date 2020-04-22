import math
import bisect



class HighPrimes():

    def __init__(self, max):
        '''
        Inicia uma instancia de HighPrimes e calcula todos os highprimes ate max
        :param max: int
        '''
        self.max = max
        self.fator = int(math.sqrt(max))
        self.primes = self.sieve()
        self.high_primesD, self.high_primesL = self.gen_highprimes()


    def sieve(self):
        '''
        Cria um Array booleano "prime[0..n]" e inicializa
        todas as entradas como True. Um valor em prime[i] sera
        definido para False caso i nao seja primo.
        :return: Array booleano
        '''
        prime = [True for i in range(self.fator + 1)]
        p = 2
        while (p * p <= self.fator):

            # Se prime[p] nao for alterado, entao p e primo.
            if (prime[p] == True):

                # Define todos os multiplos de p como False.
                for i in range(p * 2, self.fator + 1, p):
                    prime[i] = False
            p += 1
        # Define 0 e 1 como False, visto que nao sao primos.
        prime[0] = False
        prime[1] = False

        return prime

    def gen_highprimes(self):
        '''
        Calcula todos os highprimes ate self.max, retornando
        um dicionario e uma lista. Sendo estes:
        Dicionario:
        high_primesD[i] = Numero de high primes ate i
        Lista:
        high_primesL[numero de high primes ate i] = i
        :return: Dicionario, lista
        '''
        high_primesD = {}
        high_primesL = []


        qtd = 0
        for i in range(1,self.fator+1):
                if self.primes[i]:
                    high_primesD[i*i] = qtd
                    qtd += 1

                    high_primesL.append(i*i)
        return high_primesD, high_primesL

    def qtd(self, low, high):
        '''
        Dadas as fronteiras low e high, calcula quantos highprimes existem entre elas.
        :param low: int
        :param high: int
        :return: int
        '''

        try:
            # Verifica se low e um highprime
            l = self.high_primesD[low]
        except KeyError:
            # Encontra o highprime consecutivo
            l = bisect.bisect_right(self.high_primesL, low)

        try:
            # Verifica se high e um highprime
            h = self.high_primesD[high]+1
        except KeyError:
            # Encontra o highprime anterior
            h = bisect.bisect_left(self.high_primesL, high)

        return h-l



MAX_DEF = 1000000000000 # Valor maximo definido pelo problema, 10ˆ12

high = HighPrimes(MAX_DEF)
cases = int(input())
for i in range(cases):
    min, max = input().split()
    min = int(min)
    max = int(max)
    print (high.qtd(min, max))
