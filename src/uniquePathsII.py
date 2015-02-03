class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer

    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        if m == 0:
            return 0
        n = len(obstacleGrid[0])
        if n == 0 or obstacleGrid[0][0] or obstacleGrid[m-1][n-1]:
            return 0
        for i in xrange(m):
            for j in xrange(n):
                if i == 0 and j == 0:
                    obstacleGrid[i][j] = 1
                    continue
                if obstacleGrid[i][j]:
                    obstacleGrid[i][j] = 0
                else:
                    if i > 0:
                        obstacleGrid[i][j] += obstacleGrid[i-1][j]
                    if j > 0:
                        obstacleGrid[i][j] += obstacleGrid[i][j-1]
        return obstacleGrid[m-1][n-1]
