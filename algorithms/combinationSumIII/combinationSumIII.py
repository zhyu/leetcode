class Solution:
    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}

    def combinationSum3(self, k, n):
        return [arr for arr in ([j+1 for j in xrange(10) if i & (1 << j)]
                                for i in xrange(1, 512) if bin(i).count('1') == k)
                if sum(arr) == n]
