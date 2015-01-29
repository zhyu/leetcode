# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []


class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node

    def __init__(self):
        self._graph = {}

    def cloneGraph(self, node):
        if not node:
            return None
        head = UndirectedGraphNode(node.label)
        self._graph[node] = head
        for neighbor in node.neighbors:
            if neighbor not in self._graph:
                self.cloneGraph(neighbor)
            head.neighbors.append(self._graph[neighbor])
        return head
