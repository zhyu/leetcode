class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean

    def search(self, A, target):
        if not A:
            return False
        n = len(A)
        l, r = 0, n-1
        while l <= r:
            mid = (l+r)/2
            if A[mid] == target:
                return True
            if A[mid] < A[r]:
                if target <= A[r] and target > A[mid]:
                    l = mid+1
                else:
                    r = mid-1
            elif A[mid] > A[r]:
                if target >= A[l] and target < A[mid]:
                    r = mid-1
                else:
                    l = mid+1
            else:
                r -= 1
        return False
