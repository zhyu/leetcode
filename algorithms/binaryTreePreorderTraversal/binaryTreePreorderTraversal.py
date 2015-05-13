# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param root, a tree node
    # @return a list of integers

    def preorderTraversal(self, root):
        res = []
        stk = [root]
        while stk:
            n = stk.pop()
            if n:
                res.append(n.val)
                stk.append(n.right)
                stk.append(n.left)
        return res
