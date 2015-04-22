class Solution:
    # @param {integer} n
    # @return {boolean}

    def isHappy(self, n):
        square = {x: x**2 for x in xrange(10)}
        s = set()
        while n > 1 and n not in s:
            s.add(n)
            n = sum(square[x] for x in map(int, str(n)))
        return n == 1
