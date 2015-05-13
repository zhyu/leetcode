class Solution:
    # @return an integer

    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        cnt = set()
        res = 1
        l = r = 0
        n = len(s)
        while r < n:
            if s[r] not in cnt:
                res = max(r-l+1, res)
                cnt.add(s[r])
                r += 1
            else:
                while s[l] != s[r]:
                    cnt.remove(s[l])
                    l += 1
                l += 1
                r += 1
        return res
