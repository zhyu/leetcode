class Solution:
    # @param s, a string
    # @return an integer

    def numDecodings(self, s):
        if not s or s[0] == '0':
            return 0
        n = len(s)
        dp = [0] * (n+1)
        dp[0] = dp[1] = 1
        for i in xrange(1, n):
            if 10 <= int(s[i-1:i+1]) <= 26 and s[i] != '0':
                dp[i+1] = dp[i]+dp[i-1]
            elif s[i-1:i+1] == '10' or s[i-1:i+1] == '20':
                dp[i+1] = dp[i-1]
            elif s[i] != '0':
                dp[i+1] = dp[i]
            else:
                return 0
        return dp[n]
