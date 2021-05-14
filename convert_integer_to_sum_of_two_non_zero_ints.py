class Solution:
    def has_0(self, num):
        while num:
            digit = int(num % 10)
            if digit == 0:
                return True
            num = int(num / 10)
        return False

    def getNoZeroIntegers(self, n: int) -> List[int]:
        x, y = 1, n-1
        while self.has_0(x) or self.has_0(y):
            x += 1
            y -= 1
        return [x, y]