class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}

    def isIsomorphic(self, s, t):
        d1 = {}
        d2 = {}
        l = len(s)
        for i in xrange(l):
            if d1.setdefault(s[i], t[i]) != t[i]:
                return False
            if d2.setdefault(t[i], s[i]) != s[i]:
                return False
        return True
