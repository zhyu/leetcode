# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param root, a tree node
    # @return an integer

    def maxPathSum(self, root):
        self.res = root.val if root else 0
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if root is None:
            return 0
        l_max = max(0, self.dfs(root.left))
        r_max = max(0, self.dfs(root.right))
        self.res = max(self.res, root.val+l_max+r_max)
        return root.val+max(l_max, r_max)
