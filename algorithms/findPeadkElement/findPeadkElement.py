class Solution:
    # @param num, a list of integer
    # @return an integer

    def findPeakElement(self, num):
        l, r = 0, len(num)-1
        while l < r:
            m = (l+r) / 2
            if m == 0 or num[m] > num[m-1]:
                if m == r or num[m] > num[m+1]:
                    return m
                l = m + 1
            else:
                r = m - 1
        return l
