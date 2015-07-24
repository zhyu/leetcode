class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}

    def searchMatrix(self, matrix, target):
        n = len(matrix)
        m = len(matrix[0])
        x = n-1
        y = 0
        while x >= 0 and y < m:
            if matrix[x][y] == target:
                return True
            if matrix[x][y] > target:
                x -= 1
            else:
                y += 1
        return False
