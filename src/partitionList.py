# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode

    def partition(self, head, x):
        head1, head2 = ListNode(0), ListNode(0)
        last1, last2 = head1, head2
        while head:
            if head.val < x:
                last1.next = head
                head = head.next
                last1 = last1.next
                last1.next = None
            else:
                last2.next = head
                head = head.next
                last2 = last2.next
                last2.next = None
        last1.next = head2.next
        return head1.next
