class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack)==0

    def push(self,data):
        return self.stack.append(data)

    def peek(self):
        if not self.stack.isEmpty():
            return self.stack[-1]
        return "Stack is Empty"
s = Stack()
