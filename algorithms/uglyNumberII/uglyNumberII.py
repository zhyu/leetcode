class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        h = [1]
        s = set([1])
        while n > 1:
            now = heapq.heappop(h)
            for k in (2, 3, 5):
                nxt = now * k
                if nxt not in s:
                    heapq.heappush(h, nxt)
                    s.add(nxt)
            n -= 1
        return h[0]
