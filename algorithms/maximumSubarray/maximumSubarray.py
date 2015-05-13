class Solution:
    # @param A, a list of integers
    # @return an integer

    def maxSubArray(self, A):
        res = pre = A[0]
        for i in xrange(1, len(A)):
            pre = pre + A[i] if pre > 0 else A[i]
            res = max(res, pre)
        return res
