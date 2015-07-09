class Solution:
    # @param {integer[]} ratings
    # @return {integer}

    def candy(self, ratings):
        n = len(ratings)
        res = [1] * n
        j = 0
        for i in xrange(n):
            if i > 0 and ratings[i] > ratings[i-1]:
                j += 1
                res[i] = max(res[i], j)
            else:
                j = 1
        for i in reversed(xrange(n)):
            if i < n-1 and ratings[i] > ratings[i+1]:
                j += 1
                res[i] = max(res[i], j)
            else:
                j = 1
        return sum(res)
