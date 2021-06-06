class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        MAX = 100000
        m = len(dungeon)
        n = len(dungeon[0])
        result = [[-1 for i in range(n)] for j in range(m)]
        print(result)
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if i == m -1 and j == n - 1:
                    result[i][j] = max(1, 1 - dungeon[i][j])
                    continue
                if j == n - 1:
                    right = MAX
                else:
                    right = result[i][j+1]
                if i == m - 1:
                    bottom = MAX
                else:
                    bottom = result[i+1][j]
                
                x1 = right - dungeon[i][j]
                x2 = bottom - dungeon[i][j]
                result[i][j] = max(1, min(x1, x2))
        print(result)
        return result[0][0]
