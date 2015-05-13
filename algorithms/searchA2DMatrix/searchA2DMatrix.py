class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean

    def searchMatrix(self, matrix, target):
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m*n-1
        while l <= r:
            mid = (l+r)/2
            row, col = mid/n, mid % n
            if matrix[row][col] < target:
                l = mid+1
            elif matrix[row][col] > target:
                r = mid-1
            else:
                return True
        return False
