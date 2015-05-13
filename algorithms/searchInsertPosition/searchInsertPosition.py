class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer

    def searchInsert(self, A, target):
        l, r = 0, len(A)-1
        while l <= r:
            mid = (l+r)/2
            if A[mid] < target:
                l = mid+1
            elif A[mid] > target:
                r = mid-1
            else:
                return mid
        return l
