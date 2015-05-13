class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers

    def spiralOrder(self, matrix):
        res = []
        if not matrix:
            return res
        m = len(matrix)
        if m == 0:
            return res
        n = len(matrix[0])
        if n == 0:
            return res
        r = c = 0
        while r < (m+1)/2 and c < (n+1)/2:
            for i in xrange(c, n-c):
                res.append(matrix[r][i])
            for i in xrange(r+1, m-r-1):
                res.append(matrix[i][n-c-1])
            for i in reversed(xrange(c, n-c)):
                if m-r-1 == r:
                    break
                res.append(matrix[m-r-1][i])
            for i in reversed(xrange(r+1, m-r-1)):
                if n-c-1 == c:
                    break
                res.append(matrix[i][c])
            r += 1
            c += 1
        return res
