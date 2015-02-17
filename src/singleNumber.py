import operator


class Solution:
    # @param A, a list of integer
    # @return an integer

    def singleNumber(self, A):
        return reduce(operator.xor, A)
