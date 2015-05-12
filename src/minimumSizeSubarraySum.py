class Solution:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}

    def minSubArrayLen(self, s, nums):
        if not nums:
            return 0
        n = len(nums)
        i = j = cur = 0
        res = n+1
        while j < n:
            cur += nums[j]
            while cur >= s and i <= j:
                res = min(res, j-i+1)
                cur -= nums[i]
                i += 1
            j += 1
        if res == n+1:
            res = 0
        return res
