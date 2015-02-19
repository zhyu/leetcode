class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer

    def strStr(self, haystack, needle):
        n, m = len(haystack), len(needle)
        if n < m:
            return -1
        i = j = k = 0
        while i+m <= n:
            while j < m and haystack[k] == needle[j]:
                k += 1
                j += 1
            if j == m:
                return i
            i += 1
            k = i
            j = 0
        return -1
