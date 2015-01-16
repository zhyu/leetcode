class Solution:
    # @return a string

    def convertToTitle(self, num):
        res, base = '', ord('A')
        while num:
            num -= 1
            num, remainder = num / 26, num % 26
            res += chr(base + remainder)
        return res[::-1]
