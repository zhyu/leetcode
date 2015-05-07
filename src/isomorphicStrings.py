class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}

    def isIsomorphic(self, s, t):
        d1 = {}
        d2 = {}
        for i, j in zip(s, t):
            if d1.setdefault(i, j) != j or d2.setdefault(j, i) != i:
                return False
        return True
