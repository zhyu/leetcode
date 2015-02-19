class Solution:
    # @return a string

    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        return reduce(self.lcs, strs)

    def lcs(self, sa, sb):
        res = 0
        for i in xrange(min(len(sa), len(sb))):
            if sa[i] != sb[i]:
                break
            res += 1
        return sa[:res]
