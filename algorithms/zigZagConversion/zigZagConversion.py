class Solution:
    # @return a string

    def convert(self, s, nRows):
        matrix = [[] for _ in xrange(nRows)]
        idx, n = 0, len(s)
        for pos in itertools.cycle(range(nRows)+range(nRows-2, 0, -1)):
            if idx == n:
                break
            matrix[pos].append(s[idx])
            idx += 1
        return ''.join([''.join(row) for row in matrix])
