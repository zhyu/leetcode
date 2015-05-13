# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param root, a tree node
    # @return a list of integers

    def rightSideView(self, root):
        res = []

        def dfs(root, level):
            if not root:
                return
            if len(res) == level:
                res.append(root.val)
            dfs(root.right, level+1)
            dfs(root.left, level+1)

        dfs(root, 0)
        return res
