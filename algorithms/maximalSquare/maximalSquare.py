class Solution:
    # @param {character[][]} matrix
    # @return {integer}

    def maximalSquare(self, matrix):
        if not matrix:
            return 0
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                matrix[i][j] = int(matrix[i][j])
                if matrix[i][j] and i and j:
                    matrix[i][j] += min(
                        matrix[i][j-1],
                        matrix[i-1][j],
                        matrix[i-1][j-1])
        return max(map(max, matrix)) ** 2
