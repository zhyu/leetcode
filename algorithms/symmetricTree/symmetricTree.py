# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param root, a tree node
    # @return a boolean

    def isSymmetric(self, root):
        if not root:
            return True
        return self.check(root.left, root.right)

    def check(self, left, right):
        if left is None or right is None:
            return left is right
        return (left.val == right.val and
                self.check(left.left, right.right) and
                self.check(left.right, right.left))
