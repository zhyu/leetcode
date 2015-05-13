class Solution:
    # @return a list of lists of integer

    def generateMatrix(self, n):
        if n == 0:
            return []
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        cur = cur_d = 0
        cur_x = cur_y = 0
        matrix = [[0 for col in xrange(n)] for row in xrange(n)]
        while cur != n*n:
            cur += 1
            matrix[cur_x][cur_y] = cur
            nx = cur_x + dirs[cur_d][0]
            ny = cur_y + dirs[cur_d][1]
            if nx < 0 or ny < 0 or nx == n or ny == n or matrix[nx][ny]:
                cur_d = (cur_d+1) % 4
                nx = cur_x + dirs[cur_d][0]
                ny = cur_y + dirs[cur_d][1]
            cur_x, cur_y = nx, ny
        return matrix
