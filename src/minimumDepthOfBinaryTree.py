# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param root, a tree node
    # @return an integer

    def minDepth(self, root):
        if root is None:
            return 0
        q = collections.deque([(root, 1)])
        while len(q) != 0:
            p = q.popleft()
            flag = True
            if p[0].left:
                q.append((p[0].left, p[1]+1))
                flag = False
            if p[0].right:
                q.append((p[0].right, p[1]+1))
                flag = False
            if flag:
                return p[1]
