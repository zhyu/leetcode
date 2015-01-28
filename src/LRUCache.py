class LRUCache:

    class ListNode:

        def __init__(self, val):
            self.val = val
            self.next = None
            self.prev = None

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.head = self.ListNode(-1)
        self.tail = self.ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    # @return an integer
    def get(self, key):
        if key in self.cache:
            self._refresh(self.cache[key][1])
            return self.cache[key][0]
        return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key not in self.cache:
            self._refresh(self.ListNode(key))
            self.size += 1
        else:
            self._refresh(self.cache[key][1])
        self.cache[key] = [value, self.head.next]
        if self.size > self.capacity:
            node = self.tail.prev
            del self.cache[node.val]
            self._delete_node(node)
            self.size = self.capacity

    def _refresh(self, node):
        if self.head.next == node:
            return
        if node.next:
            self._delete_node(node)
        node.prev = self.head
        node.next = self.head.next
        self.head.next = node
        node.next.prev = node

    def _delete_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
