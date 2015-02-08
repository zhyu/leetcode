class Solution:
    # @return a string

    def longestPalindrome(self, s):
        n = len(s)
        if n <= 1:
            return s
        m_len = 0
        for i in xrange(n):
            l, r = self.findPalindrome(s, i, i)
            if r-l+1 > m_len:
                res = s[l:r+1]
                m_len = r-l+1
            l, r = self.findPalindrome(s, i, i+1)
            if r-l+1 > m_len:
                res = s[l:r+1]
                m_len = r-l+1
        return res

    def findPalindrome(self, s, l, r):
        n = len(s)
        while l >= 0 and r < n and s[l] == s[r]:
            l -= 1
            r += 1
        return l+1, r-1
