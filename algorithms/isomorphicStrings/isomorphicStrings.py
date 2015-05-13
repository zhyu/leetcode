class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}

    def isIsomorphic(self, s, t):
        d1 = {}
        d2 = {}
        return all(d1.setdefault(i, j) == j and d2.setdefault(j, i) == i
                   for i, j in zip(s, t))
