class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer

    def removeElement(self, A, elem):
        l, r = 0, len(A)-1
        while l <= r:
            if A[l] == elem:
                A[l] = A[r]
                r -= 1
                continue
            l += 1
        return r+1
