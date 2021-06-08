class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        start = 0
        end = n - 1
        t = [[-1 for i in range(n)] for j in range(n)]
        s = [[-1 for i in range(n)] for j in range(n)]
        def KS(i, j, _sum, alex):
            if i > j:
                return False
            if i == j:
                if alex:
                    t[i][j] = piles[i] + _sum[0] > _sum[1]
                    return t[i][j]
                else:
                    s[i][j] = _sum[0] > piles[i] + _sum[1]
                    return s[i][j]
            if alex:
                if t[i][j] == -1:
                    t[i][j] = KS(i+1, j, [_sum[0] + piles[i], _sum[1]], not alex) or KS(i, j-1, [_sum[0] + piles[j], _sum[1]], not alex)
                return t[i][j]
            else:
                if s[i][j] == -1:
                    s[i][j] = KS(i+1, j, [_sum[0], piles[i] + _sum[1]], not alex) or KS(i, j-1, [_sum[0], piles[j] + _sum[1]], not alex)
                return s[i][j]
        
        return KS(start, end, [0, 0], True)
