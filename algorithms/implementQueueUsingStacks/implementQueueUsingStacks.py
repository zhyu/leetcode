class Queue:
    # initialize your data structure here.

    def __init__(self):
        self.stk1 = []
        self.stk2 = []
        self.head = None

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.stk1.append(x)
        if self.head is None:
            self.head = x

    # @return nothing
    def pop(self):
        while len(self.stk1):
            self.stk2.append(self.stk1.pop())
        self.stk2.pop()
        self.head = None
        while len(self.stk2):
            self.push(self.stk2.pop())

    # @return an integer
    def peek(self):
        return self.head

    # @return an boolean
    def empty(self):
        return len(self.stk1) == 0
