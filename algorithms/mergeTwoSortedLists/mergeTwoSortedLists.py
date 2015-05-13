# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @param two ListNodes
    # @return a ListNode

    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val < l2.val:
            head, l1 = l1, l1.next
        else:
            head, l2 = l2, l2.next
        head.next = self.mergeTwoLists(l1, l2)
        return head
