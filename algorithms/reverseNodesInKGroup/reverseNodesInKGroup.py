# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode

    def reverseKGroup(self, head, k):
        if not head or k <= 1:
            return head
        pre_head = helper = ListNode(0)
        helper.next = head
        p = head
        count = 0

        def reverse(st, ed):
            head, tail = ed, st
            pre, cur = st, st.next
            while pre != ed:
                nxt, cur.next = cur.next, pre
                cur, pre = nxt, cur
            return head, tail

        while p:
            count += 1
            if count == k:
                nxt = p.next
                head, tail = reverse(head, p)
                pre_head.next = head
                tail.next = head = p = nxt
                pre_head = tail
                count = 0
            else:
                p = p.next
        return helper.next
