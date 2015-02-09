class Solution:
    # @return a list of lists of integers

    def combine(self, n, k):
        self.solution = []
        self.res = []
        self.dfs(n, k)
        return self.res

    def dfs(self, n, k):
        if k == 0:
            self.res.append(sorted(self.solution))
            return
        for i in xrange(n, 0, -1):
            self.solution.append(i)
            self.dfs(i-1, k-1)
            self.solution.pop()
