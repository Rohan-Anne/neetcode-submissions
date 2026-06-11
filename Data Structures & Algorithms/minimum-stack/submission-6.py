class MinStack:

    def __init__(self):
        self.currentMin = []
        self.stack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.currentMin:
            self.currentMin.append(len(self.stack) - 1)
        else:
            if self.stack[-1] < self.stack[self.currentMin[-1]]:
                self.currentMin.append(len(self.stack) - 1)
            
    def pop(self) -> None:
        if self.currentMin[-1] == len(self.stack) - 1:
            self.currentMin.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.stack[self.currentMin[-1]]
        
