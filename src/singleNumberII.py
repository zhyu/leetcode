class Solution:
    # @param A, a list of integer
    # @return an integer

    def singleNumber(self, A):
        one = two = 0
        for a in A:
            two |= (one & a)
            one ^= a
            not_three = ~(one & two)
            one &= not_three
            two &= not_three
        return one
