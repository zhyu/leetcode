class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.

    def setZeroes(self, matrix):
        if not matrix:
            return
        n = len(matrix)
        if n == 0:
            return
        m = len(matrix[0])
        pos = None
        for i in xrange(n):
            for j in xrange(m):
                if matrix[i][j] == 0:
                    if pos:
                        matrix[i][pos[1]] = 0
                        matrix[pos[0]][j] = 0
                    else:
                        pos = (i, j)
        if not pos:
            return
        for i in xrange(n):
            if i == pos[0]:
                continue
            for j in xrange(m):
                if j == pos[1]:
                    continue
                if matrix[pos[0]][j] == 0 or matrix[i][pos[1]] == 0:
                    matrix[i][j] = 0

        for i in xrange(n):
            matrix[i][pos[1]] = 0
        for j in xrange(m):
            matrix[pos[0]][j] = 0
