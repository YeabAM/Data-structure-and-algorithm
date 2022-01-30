class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = []               

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minimum or val <= self.minimum[-1]:
            self.minimum.append(val)
        

    def pop(self) -> None:
        last = self.stack[-1]
        if last == self.minimum[-1]:
            self.minimum.pop()
        return self.stack.pop()

    def top(self) -> int:
        topElement = self.stack.pop()
        self.stack.append(topElement)
        return topElement
    def getMin(self) -> int:
        return self.minimum[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()