class Solution:
    # @param num, a list of integer
    # @return an integer

    def findMin(self, num):
        n = len(num)
        l, r = 0, n-1
        res = num[0]
        while l <= r:
            mid = (l+r)/2
            if num[mid] < num[r]:
                res = min(res, num[mid])
                r = mid-1
            else:
                res = min(res, num[r])
                l = mid+1
        return res
