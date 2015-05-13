class Solution:
    # @param dungeon, a list of lists of integers
    # @return a integer

    def calculateMinimumHP(self, dungeon):
        n, m = len(dungeon), len(dungeon[0])
        dungeon[n - 1][m - 1] = max(-dungeon[n - 1][m - 1], 0)

        for i in xrange(n - 2, -1, -1):
            dungeon[i][
                m - 1] = max(dungeon[i + 1][m - 1] - dungeon[i][m - 1], 0)

        for i in xrange(m - 2, -1, -1):
            dungeon[
                n - 1][i] = max(dungeon[n - 1][i + 1] - dungeon[n - 1][i], 0)

        for i in xrange(n - 2, -1, -1):
            for j in xrange(m - 2, -1, -1):
                dungeon[i][j] = max(
                    min(dungeon[i + 1][j], dungeon[i][j + 1]) - dungeon[i][j],
                    0
                )

        return dungeon[0][0] + 1
