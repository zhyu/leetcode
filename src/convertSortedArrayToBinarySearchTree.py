# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param num, a list of integers
    # @return a tree node

    def sortedArrayToBST(self, num):
        n = len(num)
        self.num = num
        return self.convert(0, n-1)

    def convert(self, l, r):
        if l > r:
            return None
        mid = l+((r-l+1) >> 1)
        root = TreeNode(self.num[mid])
        root.left = self.convert(l, mid-1)
        root.right = self.convert(mid+1, r)
        return root
