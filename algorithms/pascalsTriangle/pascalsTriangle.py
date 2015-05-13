class Solution:
    # @return a list of lists of integers

    def generate(self, numRows):
        if numRows <= 0:
            return []
        res = [[1]]
        for i in xrange(1, numRows):
            line = [1]
            for j in xrange(1, i+1):
                if j == i:
                    line.append(1)
                    res.append(line)
                else:
                    line.append(res[i-1][j-1]+res[i-1][j])
        return res
