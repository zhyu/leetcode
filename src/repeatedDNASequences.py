class Solution:
    # @param s, a string
    # @return a list of strings

    def findRepeatedDnaSequences(self, s):
        n = len(s)
        if n <= 10:
            return []
        s2i = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        l = [s2i[ch] for ch in s]
        base = [4 ** i for i in xrange(10)]
        now = 0
        for i in xrange(10):
            now += l[i] * base[i]
        cnt = collections.defaultdict(int)
        cnt[now] = 1
        for i in xrange(10, n):
            now >>= 2
            now += l[i] * base[9]
            cnt[now] += 1
        return map(self.restore, filter(lambda x: x[1] > 1, cnt.items()))

    def restore(self, n):
        i2s = 'ACGT'
        res = ['A'] * 10
        idx = 0
        n = n[0]
        while n:
            res[idx] = i2s[n % 4]
            idx, n = idx+1, n/4
        return ''.join(res)
