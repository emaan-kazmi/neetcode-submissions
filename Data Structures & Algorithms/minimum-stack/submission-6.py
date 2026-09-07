class MinStack:

    def __init__(self):
        self.min = float('inf')
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
        else:
            self.stack.append(val - self.min)
        if val < self.min:
            self.min = val

    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
            if val < 0:
                self.min = self.min - val
            if not self.stack:
                self.min = float('inf')

    def top(self) -> int:
        top = self.stack[-1]
        if top < 0:
            return self.min
        else:
            return top + self.min

    def getMin(self) -> int:
        return self.min
        
