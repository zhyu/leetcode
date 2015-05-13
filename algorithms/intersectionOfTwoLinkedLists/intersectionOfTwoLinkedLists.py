# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @param two ListNodes
    # @return the intersected ListNode

    def getIntersectionNode(self, headA, headB):
        la, lb = self.getLen(headA), self.getLen(headB)
        if la > lb:
            for _ in xrange(lb, la):
                headA = headA.next
        elif la < lb:
            for _ in xrange(la, lb):
                headB = headB.next
        while headA:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None

    def getLen(self, head):
        l = 0
        while head:
            l += 1
            head = head.next
        return l
