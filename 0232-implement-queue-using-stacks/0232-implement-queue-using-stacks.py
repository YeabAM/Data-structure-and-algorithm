class MyQueue:
    def __init__(self):
        self.stack_A = deque([])
        self.stack_B = deque([])

    def push(self, x: int) -> None:
        while self.stack_A:
            self.stack_B.append( self.stack_A.pop() )
        self.stack_A.append( x )
        while self.stack_B:
            self.stack_A.append( self.stack_B.pop() )

    def pop(self) -> int:
        return self.stack_A.pop()

    def peek(self) -> int:
        return self.stack_A[-1]

    def empty(self) -> bool:
        return not self.stack_A and not self.stack_B