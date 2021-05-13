class Solution:
    def getCount(self, n):
        if n <= 1:
            return 1
        if self.arr[n-1] == -1:
            self.arr[n-1] = self.getCount(n-1)
        if self.arr[n-2] == -1:
            self.arr[n-2] = self.getCount(n-2)
        return self.arr[n-1] + self.arr[n-2]

    def climbStairs(self, n: int) -> int:
        self.arr = [ -1 ] * n
        print(self.arr)
        ans = self.getCount(n)
        print(self.arr)
        return ans