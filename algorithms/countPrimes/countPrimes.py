class Solution:
    # @param {integer} n
    # @return {integer}

    def countPrimes(self, n):
        primes = [0, 0] + [1] * (n-2)
        for i in xrange(2, n):
            if primes[i] == 0:
                continue
            for j in xrange(i+i, n, i):
                primes[j] = 0
        return sum(primes)
