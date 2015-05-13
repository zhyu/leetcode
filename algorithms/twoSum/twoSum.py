class Solution:
    # @return a tuple, (index1, index2)

    def twoSum(self, num, target):
        pos = {n: i for i, n in enumerate(num)}
        for i, n in enumerate(num):
            if target-n in pos and pos[target-n] > i:
                return i+1, pos[target-n]+1
