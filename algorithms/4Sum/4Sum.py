class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]

    def fourSum(self, num, target):
        if not num:
            return []
        n = len(num)
        if n < 4:
            return []
        num.sort()
        s = set()
        for i in xrange(n):
            for j in xrange(i+1, n):
                l, r = j+1, n-1
                while l < r:
                    x = num[i]+num[j]+num[l]+num[r]
                    if x == target:
                        s.add((num[i], num[j], num[l], num[r]))
                        l += 1
                        r -= 1
                    elif x > target:
                        r -= 1
                    else:
                        l += 1
        return map(list, s)
