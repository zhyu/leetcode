class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def singleNumber(self, nums):
        xor = reduce(operator.xor, nums)
        res = reduce(operator.xor, (x for x in nums if x & xor & -xor))
        return [res, res ^ xor]
