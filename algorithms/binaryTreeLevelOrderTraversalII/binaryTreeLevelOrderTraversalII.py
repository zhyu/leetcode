# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param root, a tree node
    # @return a list of lists of integers

    def levelOrderBottom(self, root):
        self.res = []
        self._dfs(root, 0)
        return reversed(self.res)

    def _dfs(self, root, level):
        if not root:
            return
        if len(self.res) == level:
            self.res.append([root.val])
        else:
            self.res[level].append(root.val)
        self._dfs(root.left, level+1)
        self._dfs(root.right, level+1)
