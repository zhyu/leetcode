class Solution:
    # @return an integer as the maximum profit

    def maxProfit(self, k, prices):
        n = len(prices)
        if n < 2:
            return 0
        if k > n/2:
            res = 0
            for i in xrange(1, n):
                res += max(prices[i]-prices[i-1], 0)
            return res
        dp = [[0, 0] for row in xrange(n)]
        for j in xrange(1, k+1):
            dp[0][j % 2] = 0
            max_profit = -prices[0]
            for i in xrange(1, n):
                dp[i][j % 2] = max(dp[i-1][j % 2], prices[i]+max_profit)
                max_profit = max(max_profit, dp[i][(j+1) % 2]-prices[i])
        return dp[n-1][k % 2]
