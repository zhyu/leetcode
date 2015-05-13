class Solution:
    # @return an integer

    def divide(self, dividend, divisor):
        if divisor == 0:
            return 2147483647
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            tmp, i = divisor, 1
            while dividend >= tmp:
                dividend -= tmp
                res += i
                tmp <<= 1
                i <<= 1
        if not positive:
            res = -res
        return min(max(res, -2147483648), 2147483647)
