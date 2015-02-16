# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @param head, a ListNode
    # @return a ListNode

    def insertionSortList(self, head):
        if not head:
            return head
        helper = ListNode(0)
        helper.next = cur = head
        while cur.next:
            if cur.next.val < cur.val:
                pre = helper
                while pre.next.val < cur.next.val:
                    pre = pre.next
                nxt = cur.next
                cur.next = nxt.next
                nxt.next = pre.next
                pre.next = nxt
            else:
                cur = cur.next
        return helper.next
