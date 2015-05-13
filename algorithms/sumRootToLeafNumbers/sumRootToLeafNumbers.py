# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param root, a tree node
    # @return an integer

    def sumNumbers(self, root):
        if root is None:
            return 0
        self.res = 0
        self.stk = []
        self.dfs(root)
        return self.res

    def dfs(self, root):
        self.stk.append(str(root.val))
        flag = True
        if root.left:
            flag = False
            self.dfs(root.left)
        if root.right:
            flag = False
            self.dfs(root.right)
        if flag:
            self.res += int(''.join(self.stk))
        self.stk.pop()
