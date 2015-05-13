# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @param head, a ListNode
    # @return a ListNode

    def deleteDuplicates(self, head):
        p1 = head
        while p1:
            p2 = p1.next
            while p2 and p1.val == p2.val:
                p2 = p2.next
            p1.next = p2
            p1 = p1.next
        return head
