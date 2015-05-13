class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string

    def findLadders(self, start, end, dict):
        dict.add(end)
        cur = [start]
        pres = collections.defaultdict(set)
        l = len(start)
        while cur and end not in pres:
            nxt = collections.defaultdict(set)
            for word in cur:
                for i in xrange(l):
                    for ch in string.ascii_lowercase:
                        new_word = word[:i] + ch + word[i+1:]
                        if new_word in dict and new_word not in pres:
                            nxt[new_word].add(word)
            cur = nxt
            pres.update(nxt)
        res = [[end]]
        while res and res[0][0] != start:
            res = [[p]+r for r in res for p in pres[r[0]]]
        return res
