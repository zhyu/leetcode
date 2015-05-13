# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @param head, a ListNode
    # @return a ListNode

    def sortList(self, head):
        if head is None or head.next is None:
            return head
        fast, slow = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        slow.next, slow = None, slow.next
        slow, fast = self.sortList(head), self.sortList(slow)
        return self.merge(slow, fast)

    def merge(self, head1, head2):
        if head1 is None:
            return head2
        if head2 is None:
            return head1
        p = ListNode(0)
        res = p
        while head1 and head2:
            if head1.val < head2.val:
                p.next = head1
                head1 = head1.next
            else:
                p.next = head2
                head2 = head2.next
            p = p.next
        if head1:
            p.next = head1
        elif head2:
            p.next = head2
        return res.next
