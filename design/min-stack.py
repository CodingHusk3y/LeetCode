class MinStack:

    def __init__(self):
        self.stk = []
        self.mono = []

    def push(self, val: int):
        if not self.mono or val <= self.mono[-1]:
            self.mono.append(val)
        else:
            self.mono.append(self.mono[-1])

        self.stk.append(val)

    def pop(self):
        self.stk.pop()
        self.mono.pop()

    def top(self):
        return self.stk[-1]

    def getMin(self):
        return self.mono[-1] if self.mono else None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()