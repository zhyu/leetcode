# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param root, a tree node
    # @return a boolean

    def isValidBST(self, root):
        return self.validate(root, float('-inf'), float('inf'))

    def validate(self, root, min_v, max_v):
        if root is None:
            return True

        if root.val <= min_v or root.val >= max_v:
            return False

        return (self.validate(root.left, min_v, root.val) and
                self.validate(root.right, root.val, max_v))
