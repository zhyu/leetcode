class Solution:
    # @param {string} s
    # @return {string}

    def shortestPalindrome(self, s):
        r = s[::-1]
        for i in xrange(len(s)+1):
            if s.startswith(r[i:]):
                return r[:i] + s
