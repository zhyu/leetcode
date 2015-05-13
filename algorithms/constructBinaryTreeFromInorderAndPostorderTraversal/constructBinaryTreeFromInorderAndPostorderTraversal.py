# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node

    def buildTree(self, inorder, postorder):
        self._inorder = inorder
        self._postorder = postorder
        l = len(inorder)
        return self.build(0, l-1, 0, l-1)

    def build(self, inSt, inEd, postSt, postEd):
        if inSt > inEd or postSt > postEd:
            return None
        root = TreeNode(self._postorder[postEd])
        pos = self._inorder[inSt:inEd+1].index(root.val) + inSt
        root.left = self.build(inSt, pos-1, postSt, postEd-inEd+pos-1)
        root.right = self.build(pos+1, inEd, postEd-inEd+pos, postEd-1)
        return root
