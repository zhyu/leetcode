class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers

    def combinationSum2(self, candidates, target):
        if not candidates:
            return []
        candidates.sort()
        n = len(candidates)
        res = set()

        def solve(start, target, tmp):
            if target < 0:
                return
            if target == 0:
                res.add(tuple(tmp))
                return
            for i in xrange(start, n):
                tmp.append(candidates[i])
                solve(i+1, target-candidates[i], tmp)
                tmp.pop()

        solve(0, target, [])
        return map(list, res)
