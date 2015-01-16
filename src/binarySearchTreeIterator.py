# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class BSTIterator:
    # @param root, a binary search tree's root node

    def __init__(self, root):
        self.stk = []
        self.pushLeft(root)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return self.stk

    # @return an integer, the next smallest number
    def next(self):
        top = self.stk.pop()
        if top.right:
            self.pushLeft(top.right)
        return top.val

    def pushLeft(self, node):
        if node:
            self.stk.append(node)
            self.pushLeft(node.left)

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
