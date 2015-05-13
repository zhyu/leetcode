class Solution:
    # @param s, a string
    # @return a list of strings

    def restoreIpAddresses(self, s):
        n = len(s)
        if n < 4 or n > 12:
            return []
        res = []

        def split2nums(s, cnt, cur):
            if s == '':
                return
            if cnt == 1:
                if s == '0' or (s[0] != '0' and 256 > int(s) > -1):
                    cur += s
                    res.append(cur)
            elif s[0] == '0':
                cur += '0.'
                split2nums(s[1:], cnt-1, cur)
            else:
                min_len = min(3, len(s))

                for i in xrange(1, min_len):
                    nxt = cur + s[:i] + '.'
                    split2nums(s[i:], cnt-1, nxt)

                if s[0] != '0' and 256 > int(s[:3]) > -1:
                    cur += s[:3] + '.'
                    split2nums(s[3:], cnt-1, cur)

        split2nums(s, 4, '')
        return res
