class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.master = []
        self.slave = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        while len(self.master) > 0:
            self.slave.append(self.master.pop())
        self.master.append(x)
        while len(self.slave) > 0:
            self.master.append(self.slave.pop())
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.master.pop()


    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.master[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.master) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()