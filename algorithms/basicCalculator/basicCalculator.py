class Solution:
    # @param {string} s
    # @return {integer}

    def calculate(self, s):
        i = res = 0
        signs = [1, 1]
        while i < len(s):
            if s[i].isdigit():
                st = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                res += int(s[st:i]) * signs.pop()
                continue
            if s[i] in '+-(':
                signs.append(signs[-1] * [1, -1][s[i] == '-'])
            elif s[i] == ')':
                signs.pop()
            i += 1
        return res
