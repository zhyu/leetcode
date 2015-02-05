class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]

    def threeSum(self, num):
        pos = {}
        n = len(num)
        num.sort()
        for i in xrange(n):
            for j in xrange(i+1, n):
                s = num[i]+num[j]
                if s not in pos:
                    pos[s] = []
                pos[s].append((i, j))
        res = set()
        for i, n in enumerate(num):
            if -n in pos:
                for j, k in pos[-n]:
                    if i < j:
                        res.add((n, num[j], num[k]))
        return [[a, b, c] for a, b, c in res]
