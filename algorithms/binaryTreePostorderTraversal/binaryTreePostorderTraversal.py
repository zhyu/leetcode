# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param root, a tree node
    # @return a list of integers

    def postorderTraversal(self, root):
        if root is None:
            return []
        res = []
        stk = [root]
        while stk:
            top = stk[-1]
            if top.left is None and top.right is None:
                res.append(stk.pop().val)
                continue
            if top.right:
                stk.append(top.right)
                top.right = None
            if top.left:
                stk.append(top.left)
                top.left = None
        return res
