class Solution:
    # @param {integer[]} nums
    # @return {integer[]}

    def productExceptSelf(self, nums):
        n = len(nums)
        res = [1] * n
        left = right = 1
        for i in xrange(n):
            res[i] *= left
            left *= nums[i]
            res[n-1-i] *= right
            right *= nums[n-1-i]
        return res
