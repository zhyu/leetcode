class Solution:
    # @param {integer[]} nums
    # @return {string[]}

    def summaryRanges(self, nums):
        res = []
        for num in nums:
            if not res or num-res[-1][-1] > 1:
                res += [],
            res[-1][1:] = num,
        return ['->'.join(map(str, r)) for r in res]
