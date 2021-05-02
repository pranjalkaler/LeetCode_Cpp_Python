class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.master = []
        self.slave = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.master.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        while len(self.master) > 1:
            self.slave.append(self.master.pop(0))
        x = self.master.pop(0)
        while len(self.slave) > 0:
            self.master.append(self.slave.pop(0))
        return x

    def top(self) -> int:
        """
        Get the top element.
        """
        while len(self.master) > 1:
            self.slave.append(self.master.pop(0))
        x = self.master.pop(0)
        while len(self.slave) > 0:
            self.master.append(self.slave.pop(0))
        self.master.append(x)
        return x

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.master) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()