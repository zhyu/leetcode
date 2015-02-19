class Solution:
    # @param A, a list of integers
    # @return a boolean

    def canJump(self, A):
        if not A:
            return False
        max_dist = 0
        for i in xrange(len(A)):
            if i > max_dist:
                return False
            max_dist = max(max_dist, i+A[i])
        return True
