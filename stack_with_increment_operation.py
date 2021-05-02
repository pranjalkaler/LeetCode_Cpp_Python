class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []
        self.occupied = 0

    def push(self, x: int) -> None:
        if self.occupied < self.maxSize:
            self.occupied += 1
            self.stack.append(x)
        print("After pushing {}, stack = {}, occupied: {}, maxSize: {}".format(x, self.stack, self.occupied, self.maxSize))

    def pop(self) -> int:
        if self.occupied:
            self.occupied -= 1
            x = self.stack.pop()
            print("After popping {}, stack = {}, occupied: {}".format(x, self.stack, self.occupied))
            # return self.stack.pop()
            return x
        else:
            return -1        

    def increment(self, k: int, val: int) -> None:
        temp = []
        for x in range(self.occupied):
            temp.append(self.stack.pop())
        
        if k < self.occupied:
            limit = k
        else:
            limit = self.occupied
        print("TEMP = {}, STACK = {}".format(temp, self.stack))
        while limit:
            limit -= 1
            self.stack.append(temp.pop() + val)
        while len(temp) > 0:
            self.stack.append(temp.pop())
        print("Stack after incrementing {} elements by {} = {}".format(k, val, self.stack))
            

# max = 3.......... 1 2 3 4 
# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)