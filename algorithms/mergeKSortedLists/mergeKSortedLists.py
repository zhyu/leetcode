# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @param a list of ListNode
    # @return a ListNode

    def mergeKLists(self, lists):
        if not lists:
            return None
        pq = []
        for n in lists:
            if n:
                heapq.heappush(pq, (n.val, n))
        head = p = ListNode(0)
        while pq:
            _, n = heapq.heappop(pq)
            p.next = n
            p = p.next
            if n.next:
                heapq.heappush(pq, (n.next.val, n.next))
        return head.next
