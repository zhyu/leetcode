class Solution:
    # @return a string

    def minWindow(self, S, T):
        if not S or not T:
            return ''
        n, m = len(S), len(T)
        if m > n:
            return ''
        cnt = collections.defaultdict(int)
        found = collections.defaultdict(int)
        for ch in T:
            cnt[ch] += 1
        st = i = found_num = 0
        window_size = n+1
        for j in xrange(n):
            if S[j] in cnt:
                ch = S[j]
                found[ch] += 1

                if found[ch] <= cnt[ch]:
                    found_num += 1
                if found_num == m:
                    while True:
                        if S[i] not in found:
                            i += 1
                        elif found[S[i]] > cnt[S[i]]:
                            found[S[i]] -= 1
                            i += 1
                        else:
                            break
                    if j-i+1 < window_size:
                        window_size = j-i+1
                        st = i
        if window_size <= n:
            return S[st:st+window_size]
        return ''
