class MinStack:

    def __init__(self):
        self.minimums = {}
        self.firstElement = True
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.firstElement:
            self.minimums[val] = len(self.stack) - 1
            self.firstElement = False
        else:
            lastMinimum = next(reversed(self.minimums))
            if val < lastMinimum:
                self.minimums[val] = len(self.stack) - 1
    def pop(self) -> None:
        lastMinimum = next(reversed(self.minimums))
        if self.minimums[lastMinimum] == len(self.stack) - 1:
            self.minimums.popitem()
        self.stack.pop()
        if len(self.stack) == 0:
            self.firstElement = True

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return next(reversed(self.minimums))
        
