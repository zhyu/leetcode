class Solution:
    # @param num, a list of integer
    # @return an integer

    def rob(self, num):
        res1 = res2 = 0
        for n in num:
            res1, res2 = res2+n, max(res1, res2)
        return max(res1, res2)
