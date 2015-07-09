class Solution:
    # @param {integer} n
    # @return {integer}

    def countDigitOne(self, n):
        res = prev = 0
        x = 1
        while n > 0:  # n = 23[y]xxx
            y = n % 10
            n /= 10
            if y > 1:
                res += x  # 23[2]xxx
            elif y == 1:
                res += prev + 1  # 23[1]xxx
            res += n * x  # 0[1]xxx ~ 22[1]xxx
            prev += y * x
            x *= 10
        return res
