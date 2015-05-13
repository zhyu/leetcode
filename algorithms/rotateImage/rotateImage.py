class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers

    def rotate(self, matrix):
        n = len(matrix)
        m = mm = n/2
        if n % 2:
            mm += 1
        n -= 1
        for i in xrange(m):
            for j in xrange(mm):
                (matrix[j][n-i],
                 matrix[n-i][n-j],
                    matrix[n-j][i],
                    matrix[i][j]) = (matrix[i][j],
                                     matrix[j][n-i],
                                     matrix[n-i][n-j],
                                     matrix[n-j][i])
        return matrix
