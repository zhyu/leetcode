class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}

    def findKthLargest(self, nums, k):
        k = len(nums) - k

        def quickselect(st, ed):
            pivot = nums[ed]
            pos = st
            for i in xrange(st, ed):
                if nums[i] < pivot:
                    nums[i], nums[pos] = nums[pos], nums[i]
                    pos += 1
            nums[pos], nums[ed] = nums[ed], nums[pos]
            if pos == k:
                return nums[pos]
            elif pos < k:
                return quickselect(pos+1, ed)
            else:
                return quickselect(st, pos-1)

        return quickselect(0, len(nums)-1)
