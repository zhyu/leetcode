class Solution:
    # @param {integer[]} nums
    # @return {integer}

    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]

        def rob_util(nums):
            res1 = res2 = 0
            for n in nums:
                res1, res2 = max(res1, res2), res1 + n
            return max(res1, res2)
        return max(rob_util(nums[1:]), rob_util(nums[:-1]))
