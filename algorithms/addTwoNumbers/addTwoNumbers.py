# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @return a ListNode

    def addTwoNumbers(self, l1, l2):
        return self.add(l1, l2, 0)

    def add(self, l1, l2, adder):
        if l1 is None and l2 is None and adder == 0:
            return None

        res = ListNode(adder)
        if l1:
            res.val += l1.val
        if l2:
            res.val += l2.val
        adder = res.val/10
        res.val %= 10
        res.next = self.add(
            l1.next if l1 else None,
            l2.next if l2 else None,
            adder)
        return res
