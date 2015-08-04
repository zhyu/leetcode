class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}

    def canFinish(self, numCourses, prerequisites):
        g = {v: [] for v in xrange(numCourses)}
        deg = {v: 0 for v in xrange(numCourses)}
        s = set(range(numCourses))
        for u, v in prerequisites:
            g[u].append(v)
            deg[v] += 1
            s.discard(v)
        cnt = 0
        while s:
            cnt += 1
            u = s.pop()
            for v in g[u]:
                deg[v] -= 1
                if deg[v] == 0:
                    s.add(v)
        return cnt == numCourses
