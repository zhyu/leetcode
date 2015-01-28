class Solution:
    # @param A, a list of integers
    # @return an integer

    def maxProduct(self, A):
        if not A:
            return 0
        if len(A) == 1:
            return A[0]

        maxV, minV = A[0], A[0]
        res = maxV
        for val in A[1:]:
            if val > 0:
                maxV, minV = max(val, maxV * val), min(val, minV * val)
            else:
                maxV, minV = max(val, minV * val), min(val, maxV * val)
            res = max(res, maxV)
        return res
