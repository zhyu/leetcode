# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode

    def rotateRight(self, head, k):
        if not head:
            return None
        n = self.len(head)
        k %= n
        if k == 0:
            return head
        slow = fast = head
        for _ in xrange(k):
            fast = fast.next
        while fast.next:
            slow, fast = slow.next, fast.next
        head, fast.next = slow.next, head
        slow.next = None
        return head

    def len(self, head):
        res = 0
        while head:
            res += 1
            head = head.next
        return res
