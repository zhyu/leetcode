class Solution:
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings

    def fullJustify(self, words, L):
        if not words:
            return []
        words = ' '.join(words) + ' '
        res = []
        while words:
            pos = words.rfind(' ', 0, L+1)
            line = words[:pos].split()
            l, n = sum([len(w) for w in line]), len(line)
            if n == 1:
                res.append(line[0].ljust(L))
            else:
                s, remainder = divmod(L-l, n-1)
                line[:-1] = [w+' '*s for w in line[:-1]]
                line[:remainder] = [w+' ' for w in line[:remainder]]
                res.append(''.join(line))
            words = words[pos+1:]
        res[-1] = ' '.join(res[-1].split()).ljust(L)
        return res
