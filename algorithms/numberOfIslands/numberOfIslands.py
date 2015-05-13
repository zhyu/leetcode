class Solution:
    # @param grid, a list of list of characters
    # @return an integer

    def _get_f(self, x):
        if x != self.f[x]:
            self.f[x] = self._get_f(self.f[x])
        return self.f[x]

    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0
        n, m = len(grid), len(grid[0])
        self.f = [0]*(n*m)

        for i in xrange(n):
            for j in xrange(m):
                x = i * m + j
                if grid[i][j] == '1':
                    self.f[x] = x
                    if i and grid[i-1][j] == '1':
                        self.f[self._get_f(x)] = self._get_f((i-1)*m+j)
                    if j and grid[i][j-1] == '1':
                        self.f[self._get_f(x)] = self._get_f(i*m+j-1)
                else:
                    self.f[x] = -1
        return len(filter(lambda x: self.f[x] != -1 and x == self._get_f(x),
                          xrange(n*m)))
