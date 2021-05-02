class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.min = val
            self.minStack.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        x = self.stack.pop()
        if x == self.min:
            self.minStack.pop()
        else:
            # find x in minStack
            temp = []
            for y in self.stack:
                if y == x:
                    self.stack.pop()
                    break
                else:
                    temp.append(self.stack.pop())

    def top(self) -> int:
        

    def getMin(self) -> int:
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()