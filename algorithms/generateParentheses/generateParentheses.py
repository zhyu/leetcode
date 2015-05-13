class Solution:
    # @param an integer
    # @return a list of string

    def generateParenthesis(self, n):
        if n == 0:
            return []
        res = []

        def dfs(left, right, now):
            if left == n and right == n:
                res.append(now)
                return
            if left < n:
                dfs(left+1, right, now+'(')
            if right < left:
                dfs(left, right+1, now+')')
        dfs(0, 0, '')
        return res
