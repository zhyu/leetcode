class Solution:
    # @param {integer[]} nums
    # @return {integer[]}

    def majorityElement(self, nums):
        res = []
        if not nums:
            return res
        x, y = 0, 1
        x_cnt = y_cnt = 0
        for num in nums:
            if num == x:
                x_cnt += 1
            elif num == y:
                y_cnt += 1
            elif x_cnt == 0:
                x = num
                x_cnt = 1
            elif y_cnt == 0:
                y = num
                y_cnt = 1
            else:
                x_cnt -= 1
                y_cnt -= 1
        if nums.count(x) > len(nums) / 3:
            res.append(x)
        if x != y and nums.count(y) > len(nums) / 3:
            res.append(y)
        return res
