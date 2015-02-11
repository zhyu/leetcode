class Solution:
    # @return an integer

    def reverse(self, x):
        int_max = 2147483647
        limit = int_max/10
        if x > 0:
            sig = 1
        elif x < 0:
            sig = -1
            x = -x
        else:
            return x
        y = 0
        while x:
            if y > limit:
                return 0
            y = y*10 + (x % 10)
            x /= 10
        return y*sig
