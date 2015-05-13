class Solution:
    # @param num, a list of integers
    # @return an integer

    def majorityElement(self, num):
        res, cnt = num.pop(), 1
        for x in num:
            if res == x:
                cnt += 1
            else:
                cnt -= 1
                if cnt == 0:
                    res, cnt = x, 1
        return res
