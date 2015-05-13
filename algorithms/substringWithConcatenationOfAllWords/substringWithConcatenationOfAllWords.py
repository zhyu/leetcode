class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer

    def findSubstring(self, S, L):
        if not S or not L:
            return []
        word_size = len(L[0])
        if word_size == 0:
            return []
        word_num = len(L)
        total = word_size * word_num
        n = len(S)
        if total > n:
            return []
        needed = collections.defaultdict(int)
        for s in L:
            needed[s] += 1
        res = []
        for i in xrange(n):
            found = collections.defaultdict(int)
            found_num = 0
            for j in xrange(i, i+total, word_size):
                word = S[j:j+word_size]
                if word not in needed:
                    break
                else:
                    found[word] += 1
                    found_num += 1
                    if found[word] > needed[word]:
                        break
                    elif found_num == word_num:
                        res.append(i)
        return res
