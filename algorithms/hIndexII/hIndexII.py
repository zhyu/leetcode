class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        l, r = 0, n-1
        while l<=r:
            mid = (l+r) >> 1
            if citations[mid] == n - mid:
                return citations[mid]
            elif citations[mid] > n - mid:
                r = mid - 1
            else:
                l = mid + 1
        return n - l
