class Solution:
    # @return a string

    def countAndSay(self, n):
        res = '1'
        for _ in xrange(n-1):
            tmp = []
            for k, g in itertools.groupby(res):
                tmp.append(str(len(list(g)))+k)
            res = ''.join(tmp)
        return res
