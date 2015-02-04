# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @param head, a list node
    # @return a tree node

    def sortedListToBST(self, head):
        if head is None:
            return None
        if head.next is None:
            return TreeNode(head.val)
        slow, fast = head, head.next
        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
        fast, slow.next = slow.next, None
        root = TreeNode(fast.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(fast.next)
        return root
