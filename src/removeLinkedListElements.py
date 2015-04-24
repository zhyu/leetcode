# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}

    def removeElements(self, head, val):
        helper = ListNode(0)
        cur = helper
        while head:
            nxt = head.next
            head.next = None
            if head.val != val:
                cur.next = head
                cur = cur.next
            head = nxt
        return helper.next
