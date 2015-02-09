class Solution:
    # @return a boolean

    def isValid(self, s):
        left = {'(': 0, '[': 1, '{': 2}
        right = {')': 0, ']': 1, '}': 2}
        stk = []
        for ch in s:
            if ch in left:
                stk.append(ch)
            elif ch in right:
                if len(stk) == 0:
                    return False
                prev = stk.pop()
                if left.get(prev, -1) != right[ch]:
                    return False
            else:
                return False
        return len(stk) == 0
