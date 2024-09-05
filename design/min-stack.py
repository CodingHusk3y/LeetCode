class MinStack:

    def __init__(self):
        self.stk = []
        self.mono_stk = []

    def push(self, val: int) -> None:
        if not self.mono_stk or val <= self.mono_stk[-1]:
           self.mono_stk.append(val)
        else:
            self.mono_stk.append(self.mono_stk[-1])

        self.stk.append(val)

    def pop(self) -> None:
        self.mono_stk.pop()
        
        self.stk.pop()


    def top(self) -> int:
        if self.stk:
            return self.stk[-1]
        else:
            return None

    def getMin(self) -> int:
        if self.mono_stk:
            return self.mono_stk[-1]
        else:
            return None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()