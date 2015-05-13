class Solution:

    def __init__(self):
        self.res = {}

    # @return a boolean
    def isMatch(self, s, p):
        if (s, p) in self.res:
            return self.res[(s, p)]
        if p == '':
            self.res[(s, p)] = (s == '')
            return self.res[(s, p)]
        if len(p) == 1 or p[1] != '*':
            self.res[(s, p)] = (s != '' and (s[0] == p[0] or p[0] == '.') and
                                self.isMatch(s[1:], p[1:]))
            return self.res[(s, p)]
        i, n = 0, len(s)
        while i < n and (p[0] == s[i] or p[0] == '.'):
            if self.isMatch(s[i:], p[2:]):
                self.res[(s, p)] = True
                return True
            i += 1
        self.res[(s, p)] = self.isMatch(s[i:], p[2:])
        return self.res[(s, p)]
