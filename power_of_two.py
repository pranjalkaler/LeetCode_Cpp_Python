class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        while n > 1:
            print(n)
            if n % 2 != 0:
                return False
            n = int(n / 2)
        return True
