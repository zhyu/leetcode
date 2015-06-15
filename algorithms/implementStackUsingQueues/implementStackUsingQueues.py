class Stack:
    # initialize your data structure here.

    def __init__(self):
        self.stk = collections.deque()

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.stk.append(x)

    # @return nothing
    def pop(self):
        self.__rearrange()
        self.stk.popleft()

    # @return an integer
    def top(self):
        self.__rearrange()
        res = self.stk[0]
        self.stk.append(self.stk.popleft())
        return res

    # @return an boolean
    def empty(self):
        return len(self.stk) == 0

    def __rearrange(self):
        for _ in xrange(len(self.stk) - 1):
            self.stk.append(self.stk.popleft())
