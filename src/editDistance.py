class Solution:
    # @return an integer

    def minDistance(self, word1, word2):
        n, m = len(word1), len(word2)
        dp = range(m+1)
        for i in xrange(1, n+1):
            lefttop, dp[0] = dp[0], i
            for j in xrange(1, m+1):
                lefttop, dp[j] = dp[j], min(
                    min(dp[j]+1, dp[j-1]+1), lefttop+(word1[i-1] != word2[j-1]))
        return dp[m]
