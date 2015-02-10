# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param root, a tree node
    # @return a tree node

    def recoverTree(self, root):
        self.p1 = self.p2 = self.prev = None
        self.dfs(root)
        if self.p1 and self.p2:
            self.p1.val, self.p2.val = self.p2.val, self.p1.val
        return root

    def dfs(self, root):
        if root is None:
            return
        self.dfs(root.left)
        if self.prev and self.prev.val > root.val:
            if self.p1 is None:
                self.p1 = self.prev
            self.p2 = root
        self.prev = root
        self.dfs(root.right)
