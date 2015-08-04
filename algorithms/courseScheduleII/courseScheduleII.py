class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {integer[]}
    def findOrder(self, numCourses, prerequisites):
        g = {v: [] for v in xrange(numCourses)}
        deg = {v: 0 for v in xrange(numCourses)}
        s = set(range(numCourses))
        for u, v in prerequisites:
            g[v].append(u)
            deg[u] += 1
            s.discard(u)
        res = []
        while s:
            u = s.pop()
            res.append(u)
            for v in g[u]:
                deg[v] -= 1
                if deg[v] == 0:
                    s.add(v)
        return [] if len(res) != numCourses else res
