class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.

    def rotate(self, nums, k):
        if not nums:
            return
        n = len(nums)
        k %= n
        if k == 0:
            return

        def reverse(st, ed):
            while st < ed:
                nums[st], nums[ed] = nums[ed], nums[st]
                st += 1
                ed -= 1
        reverse(0, n-1)
        reverse(0, k-1)
        reverse(k, n-1)
