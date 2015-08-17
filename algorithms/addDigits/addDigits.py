class Solution:
    # @param {integer} num
    # @return {integer}

    def addDigits(self, num):
        if num == 0:
            return 0
        rem = num % 9
        if rem == 0:
            return 9
        return rem
