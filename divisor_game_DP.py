class Toggle:
    def __init__(self, val=0):
        self.val = 0
    def get(self):
        return self.val
    def flip(self):
        return 1 if self.val == 0 else 0
    def FLIP(self):
        self.val = 1 if self.val == 0 else 0
class Solution:

    def getFactors(self, n):
        factors = []
        for x in range(1, int(n/2) + 1):
            if n % x == 0:
                factors.append(x)
        return factors
            

    def divisorGame(self, n: int) -> bool:
        self.map = []
        self.map.append([ 0 ] * (n+1))
        self.map.append([ 0 ] * (n+1))
        self.map[0][1] = 0
        self.map[1][1] = 1
        i = Toggle()
        for j in range(2, n+1):
            factors = self.getFactors(j)
            VAL = val = 0
            for x in factors:
                val = self.map[i.flip()][j - x]
                VAL = VAL if VAL >= val else 1
            self.map[i.get()][j] = VAL
            i.FLIP()
        for x in self.map:
            print(x)
        return self.map[0][n]
            
            
            