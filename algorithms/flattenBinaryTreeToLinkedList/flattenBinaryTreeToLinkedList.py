# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param root, a tree node
    # @return nothing, do it in place

    def flatten(self, root):
        self.connect(root)

    def connect(self, root):
        if root is None or (root.left is None and root.right is None):
            return root
        left_end = right_end = None
        if root.left:
            left_end = self.connect(root.left)
        if root.right:
            right_end = self.connect(root.right)
        if left_end:
            left_end.right, root.right = root.right, root.left
            root.left = None
        if right_end is None:
            return left_end
        return right_end
