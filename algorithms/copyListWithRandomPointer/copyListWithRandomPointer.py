# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None


class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode

    def copyRandomList(self, head):
        if head is None:
            return None
        cur = head
        while cur:
            n_node = RandomListNode(cur.label)
            n_node.next, cur.next, cur = cur.next, n_node, cur.next
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        cur, n_node, res = head, head.next, head.next
        while cur:
            cur.next, cur = n_node.next, n_node.next
            if cur and cur.next:
                n_node.next, n_node = cur.next, cur.next
        return res
