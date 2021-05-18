class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        if n == 1:
            return start
        xor = start
        val = start
        for i in range(1, n):
            val = start + 2*i
            xor = xor ^ val
        return xor
            