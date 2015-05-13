# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param root, a tree node
    # @return a list of integers

    def inorderTraversal(self, root):
        if root is None:
            return []
        res = []
        stk = []
        p = root
        while stk or p:
            if p:
                stk.append(p)
                p = p.left
            else:
                q = stk.pop()
                res.append(q.val)
                p = q.right
        return res
