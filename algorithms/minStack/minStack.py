class MinStack:

    def __init__(self):
        self.stk = []
        self.min = []

    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.stk.append(x)
        if not self.min or self.min[-1] >= x:
            self.min.append(x)

    # @return nothing
    def pop(self):
        if self.stk[-1] == self.min[-1]:
            self.min.pop()
        self.stk.pop()

    # @return an integer
    def top(self):
        return self.stk[-1]

    # @return an integer
    def getMin(self):
        return self.min[-1]
