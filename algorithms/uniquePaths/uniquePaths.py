class Solution:
    # @return an integer

    def uniquePaths(self, m, n):
        if m == 0 or n == 0:
            return 0
        dp = [[1 for col in xrange(n)] for row in xrange(m)]
        for i in xrange(1, n):
            for j in xrange(1, m):
                dp[j][i] = dp[j-1][i] + dp[j][i-1]
        return dp[m-1][n-1]
