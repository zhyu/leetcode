class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}

    def containsNearbyDuplicate(self, nums, k):
        pos = {}
        for i, n in enumerate(nums):
            if n in pos and i-pos[n] <= k:
                return True
            pos[n] = i
        return False
