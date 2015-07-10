# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @param {ListNode} head
    # @return {boolean}

    def isPalindrome(self, head):
        rhead = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow.next, slow, rhead = rhead, slow.next, slow
        if fast:
            slow = slow.next
        while rhead and rhead.val == slow.val:
            rhead = rhead.next
            slow = slow.next
        return not rhead
