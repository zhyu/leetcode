class Solution:
    # @return an integer

    def trailingZeroes(self, n):
        res, factor, cnt = 0, 5, n
        while cnt:
            factor, cnt = factor * 5, n / factor
            res += cnt
        return res
