# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @param {ListNode} head
    # @return {ListNode}

    def reverseList(self, head):
        if head is None:
            return head
        helper = ListNode(0)

        def reverse_list(head):
            if head is None:
                return head
            prev = reverse_list(head.next)
            if prev is None:
                helper.next = head
            else:
                head.next = None
                prev.next = head
            return head

        reverse_list(head)
        return helper.next
