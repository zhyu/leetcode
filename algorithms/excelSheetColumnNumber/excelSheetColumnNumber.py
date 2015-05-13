class Solution:
    # @param s, a string
    # @return an integer

    def titleToNumber(self, s):
        base = ord('A') - 1
        return sum([(x - base) * (26 ** i)
                    for i, x in enumerate(map(ord, s[::-1]))])
