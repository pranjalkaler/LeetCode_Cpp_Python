class Solution:
    def totalMoney(self, n: int) -> int:
        f1 = int(n/7)
        f2 = int(n%7)
        total = x = 0
        
        if f1 > 0:
            for x in range(1, f1+1):
                for y in range(x, x+7):
                    total += y
        x += 1
        while f2:
            total += x
            x += 1
            f2 -= 1
        return total