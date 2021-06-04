class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n = list(bin(n)[2:])
        if len(n) == 1:
            return True
        last = n[0]
        for i in range(1, len(n)):
            if last == n[i]:
                return False
            last = n[i]
        return True
