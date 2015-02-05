class Solution:
    # @return an integer

    def threeSumClosest(self, num, target):
        num.sort()
        res = sum(num[:3])
        if res > target:
            diff = res-target
        elif res < target:
            diff = target-res
        else:
            return res
        n = len(num)
        for i in xrange(n):
            j, k = i+1, n-1
            while j < k:
                s = num[i]+num[j]+num[k]
                if s > target:
                    n_diff = s-target
                    k -= 1
                elif s < target:
                    n_diff = target-s
                    j += 1
                else:
                    return s
                if n_diff < diff:
                    res, diff = s, n_diff
        return res
