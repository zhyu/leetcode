class Solution:
    # @param a list of integers
    # @return an integer

    def removeDuplicates(self, A):
        if not A:
            return 0
        n = len(A)
        cnt = 0
        pos = 1
        for i in xrange(1, n):
            if A[i] == A[i-1]:
                cnt += 1
            else:
                A[pos] = A[i]
                pos += 1
        return n-cnt
