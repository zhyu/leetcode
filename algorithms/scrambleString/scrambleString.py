class Solution:
    # @return a boolean

    def isScramble(self, s1, s2):
        cnt = {}
        for ch in s1:
            if ch not in cnt:
                cnt[ch] = 1
            else:
                cnt[ch] += 1
        for ch in s2:
            if ch not in cnt:
                return False
            else:
                cnt[ch] -= 1
        if len(filter(int, cnt.values())) != 0:
            return False
        l = len(s1)
        if l == 1:
            return True
        for idx in xrange(1, l):
            if (self.isScramble(s1[:idx], s2[:idx]) and
                    self.isScramble(s1[idx:], s2[idx:])):
                return True
            if (self.isScramble(s1[:idx], s2[-idx:]) and
                    self.isScramble(s1[idx:], s2[:-idx])):
                return True
        return False
