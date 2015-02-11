
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers

    def pathSum(self, root, sum):
        self.res = []
        self.num = []
        self.dfs(root, sum)
        return self.res

    def dfs(self, root, sum):
        if root is None:
            return
        self.num.append(root.val)
        if root.val == sum and root.left is None and root.right is None:
            self.res.append(copy.deepcopy(self.num))
        else:
            self.dfs(root.left, sum-root.val)
            self.dfs(root.right, sum-root.val)
        self.num.pop()
