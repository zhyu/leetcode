class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        s = 0
        for num in nums:
            s += num
        return n * (n+1) / 2 - s
