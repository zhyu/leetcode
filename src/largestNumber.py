class Solution:
    # @param num, a list of integers
    # @return a string

    def largestNumber(self, num):
        return ''.join(sorted(map(str, num), cmp=self.cmp)).lstrip('0') or '0'

    def cmp(self, x, y):
        return [1, -1][x + y > y + x]
