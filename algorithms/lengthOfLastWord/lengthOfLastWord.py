class Solution:
    # @param s, a string
    # @return an integer

    def lengthOfLastWord(self, s):
        a = s.split()
        if len(a) < 1:
            return 0
        return len(a[-1])
