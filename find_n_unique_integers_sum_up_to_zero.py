class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []
        if n % 2 != 0:
            result.append(0)
            n -= 1
        i = 1
        while n:
            result.append(i)
            result.append(-i)
            n -= 2
            i += 1
        result.sort()
        return result
