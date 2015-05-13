# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @param head, a ListNode
    # @return nothing

    def reorderList(self, head):
        if head is None or head.next is None:
            return
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        fast, slow.next = slow.next, None
        fast = self.reverseList(fast)
        self.merge2Lists(head, fast)

    def reverseList(self, head):
        if head is None or head.next is None:
            return head
        pre, cur = head, head.next
        while cur:
            nxt, cur.next = cur.next, pre
            cur, pre = nxt, cur
        head.next = None
        return pre

    def merge2Lists(self, l1, l2):
        while l2:
            n1, n2 = l1.next, l2.next
            l1.next, l2.next = l2, n1
            l1, l2 = n1, n2
