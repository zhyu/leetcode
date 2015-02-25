class Solution:
    # @param path, a string
    # @return a string

    def simplifyPath(self, path):
        paths = filter(lambda x: x, path.split('/'))
        stk = []
        for path in paths:
            if path == '.':
                continue
            elif path == '..':
                if stk:
                    stk.pop()
            else:
                stk.append(path)
        return '/' + '/'.join(stk)
