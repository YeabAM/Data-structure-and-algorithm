class MinStack:

    def __init__(self):
        self.cur_min = []
        self.stack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.cur_min:
            self.cur_min.append(val)
        else:
            current_minimum = min(self.cur_min[-1], val)
            self.cur_min.append(current_minimum)
        
    def pop(self) -> None:
        self.stack.pop()
        self.cur_min.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.cur_min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()