# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param root, a tree node
    # @return a boolean

    def isBalanced(self, root):
        return self.getDepth(root) != -1

    def getDepth(self, root):
        if root is None:
            return 0
        l_depth = self.getDepth(root.left)
        if l_depth == -1:
            return -1
        r_depth = self.getDepth(root.right)
        if r_depth == -1:
            return -1
        if l_depth-r_depth > 1 or l_depth-r_depth < -1:
            return -1
        return max(l_depth, r_depth) + 1
