class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if not self.stack:
            return

        s2 = []
        n = len(self.stack)

        for _ in range(n - 1):
            s2.append(self.stack.pop())
        
        x = self.stack.pop()
        
        while s2:
            self.stack.append(s2.pop())
        
        return x

    def peek(self) -> int:
        if not self.stack:
            return

        s2 = []
        n = len(self.stack)

        for _ in range(n - 1):
            s2.append(self.stack.pop())
        
        x = self.stack.pop()
        
        self.stack.append(x)
        while s2:
            self.stack.append(s2.pop())
            
        return x

    def empty(self) -> bool:
        return len(self.stack) == 0        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()