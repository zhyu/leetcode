class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer

    def search(self, A, target):
        if not A:
            return -1
        n = len(A)
        l, r = 0, n-1
        while l <= r:
            mid = (l+r)/2
            if A[mid] == target:
                return mid
            if A[mid] < A[r]:
                if target <= A[r] and target > A[mid]:
                    l = mid+1
                else:
                    r = mid-1
            else:
                if target >= A[l] and target < A[mid]:
                    r = mid-1
                else:
                    l = mid+1
        return -1
