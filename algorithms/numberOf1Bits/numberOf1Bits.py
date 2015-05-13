class Solution:
    # @param n, an integer
    # @return an integer

    def hammingWeight(self, n):
        if n == 0:
            return 0
        return (n & 1) + self.hammingWeight(n >> 1)
