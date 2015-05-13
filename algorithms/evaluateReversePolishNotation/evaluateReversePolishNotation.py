class Solution:
    # @param tokens, a list of string
    # @return an integer

    def evalRPN(self, tokens):
        stack = []
        for t in tokens:
            if t == '+':
                stack.append(stack.pop() + stack.pop())
            elif t == '-':
                stack.append(-(stack.pop() - stack.pop()))
            elif t == '*':
                stack.append(stack.pop() * stack.pop())
            elif t == '/':
                stack.append(int(1.0 / stack.pop() * stack.pop()))
            else:
                stack.append(int(t))
        return stack.pop()
