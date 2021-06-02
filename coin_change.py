class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        MAX = 100000
        if amount == 0:
            return 0
        t = [[-1 for i in range(amount + 1)] for j in range(len(coins) + 1)]
        def KS(c, a):
            if a == 0:
                t[c][a] = 0
                return 0
            if c == 0 or a < 0:
                return MAX
            if t[c][a] != -1:
                return t[c][a]
            t[c][a] = min(1 + KS(c, a-coins[c-1]), KS(c-1, a))
            return t[c][a]
        
        result = KS(len(coins), amount)
        return -1 if result == MAX else result 
