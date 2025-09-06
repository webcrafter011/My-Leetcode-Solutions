class MinStack:

    def __init__(self):
        self.st = []
        self.minStack = [float('inf')]

    def push(self, val: int) -> None:
        self.st.append(val)

        if self.minStack[-1] >= val:
            self.minStack.append(val)
        
    def pop(self) -> None:
        if not self.st:
            return None

        if self.st[-1] == self.minStack[-1]:
            self.minStack.pop()

        return self.st.pop()

    def top(self) -> int:
        return self.st[-1] if self.st else None
        
    def getMin(self) -> int:
        return self.minStack[-1] if self.minStack else None

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
