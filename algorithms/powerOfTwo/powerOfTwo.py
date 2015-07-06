class Solution:
    # @param {integer} n
    # @return {boolean}

    def isPowerOfTwo(self, n):
        cnt = 0
        while n:
            if n & 1:
                cnt += 1
            if cnt > 1:
                return False
            n >>= 1
        return cnt == 1
