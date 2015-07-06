class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}

    def subsets(self, nums):
        n = len(nums)
        nums.sort()
        return [[x for j, x in enumerate(nums) if (1 << j) & i]
                for i in xrange(1 << n)]
