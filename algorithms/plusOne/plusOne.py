class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits

    def plusOne(self, digits):
        adder = 1
        for idx, num in enumerate(digits[::-1]):
            if adder == 0:
                break
            result = num + adder
            adder = result / 10
            digits[-1-idx] = result % 10
        if adder:
            return [1] + digits
        return digits
