class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}

    def isAnagram(self, s, t):
        return collections.Counter(s) == collections.Counter(t)
