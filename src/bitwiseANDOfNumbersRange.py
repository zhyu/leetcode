class Solution:
    # @param m, an integer
    # @param n, an integer
    # @return an integer

    def rangeBitwiseAnd(self, m, n):
        cnt = 0
        while m != n:
            m >>= 1
            n >>= 1
            cnt += 1
        return m << cnt
