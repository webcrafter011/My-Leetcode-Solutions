class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, val):
        self.stack.append(val)
    
    def pop(self):
        if not self.stack:
            return None
        
        return self.stack.pop()
    
    def size(self):
        return len(self.stack)


    def isEmpty(self):
        return len(self.stack) == 0
    

class MyQueue:

    def __init__(self):
        self.q = Stack()

    def push(self, x: int) -> None:
        self.q.push(x)

    def pop(self) -> int:
        temp = Stack()

        while self.q.size() > 1: # till second last element
            temp.push(self.q.pop())
        
        val = self.q.pop() # take the last element 

        while temp.size():
            self.q.push(temp.pop())
        
        return val

    def peek(self) -> int:
        temp = Stack()

        while self.q.size() > 1: # till second last element
            temp.push(self.q.pop())
        
        val = self.q.pop() # take the last element 

        self.q.push(val)
        while temp.size():
            self.q.push(temp.pop())
        
        
        return val

    def empty(self) -> bool:
        return self.q.isEmpty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()