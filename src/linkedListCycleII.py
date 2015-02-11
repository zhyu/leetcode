# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @param head, a ListNode
    # @return a list node

    def detectCycle(self, head):
        slow = fast = head
        no_loop = True
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                no_loop = False
                break
        if no_loop:
            return None
        fast = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
