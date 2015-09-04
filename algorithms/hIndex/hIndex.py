class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        c = collections.Counter([min(x, n) for x in citations])
        s = reduce(lambda a, x: a + [a[-1] + c[x]], reversed(range(n)), [c[n]])
        return next((n-i for i, v in enumerate(s) if v >= n-i), 0)
