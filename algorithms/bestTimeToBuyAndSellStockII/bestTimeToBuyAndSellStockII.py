class Solution:
    # @param prices, a list of integer
    # @return an integer

    def maxProfit(self, prices):
        l = len(prices)
        if l < 2:
            return 0
        cur_min = cur_max = prices[0]
        res = 0
        is_up = True
        for i in xrange(1, l):
            if is_up:
                if prices[i] > prices[i-1]:
                    cur_max = prices[i]
                else:
                    res += cur_max-cur_min
                    is_up = False
                    cur_min = prices[i]
            else:
                if prices[i] < prices[i-1]:
                    cur_min = prices[i]
                else:
                    is_up = True
                    cur_max = prices[i]
        if is_up and cur_max > cur_min:
            res += cur_max-cur_min
        return res
