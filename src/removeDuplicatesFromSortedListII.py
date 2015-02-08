# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @param head, a ListNode
    # @return a ListNode

    def deleteDuplicates(self, head):
        helper = ListNode(0)
        helper.next = head
        tail, p = helper, head
        dup = False
        while p and p.next:
            if not dup and p.val == p.next.val:
                dup = True
                p = p.next
                continue
            if dup and p.val != p.next.val:
                dup = False
                tail.next = p.next
                p = p.next
                continue
            if not dup:
                tail = p
            p = p.next
        if dup:
            tail.next = None
        return helper.next
