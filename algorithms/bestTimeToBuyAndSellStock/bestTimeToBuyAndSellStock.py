class Solution:
    # @param prices, a list of integer
    # @return an integer

    def maxProfit(self, prices):
        n = len(prices)
        if n < 2:
            return 0
        min_price = prices[0]
        res = 0
        for i in xrange(1, n):
            res = max(res, prices[i]-min_price)
            min_price = min(min_price, prices[i])
        return res
