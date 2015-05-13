class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer

    def ladderLength(self, start, end, dict):
        if not dict:
            return 0
        q = collections.deque([(start, 1)])
        dict.remove(start)
        while q:
            cur_word, cur_dist = q.popleft()
            if cur_word == end:
                return cur_dist
            for i in xrange(len(cur_word)):
                cur_char_arr = bytearray(cur_word)
                for ch in xrange(97, 123):
                    cur_char_arr[i] = ch
                    new_word = str(cur_char_arr)
                    if new_word in dict:
                        q.append((new_word, cur_dist+1))
                        dict.remove(new_word)
        return 0
