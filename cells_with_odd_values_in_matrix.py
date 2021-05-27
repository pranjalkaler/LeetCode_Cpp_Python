class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        x = [ [ 0 for i in range(n) ] for j in range(m)]
        print(x)
        odds = 0
        for ind in indices:
            for i in range(n):
                x[ind[0]][i] += 1
                if x[ind[0]][i] % 2 == 0:
                    odds -= 1
                else:
                    odds += 1
                # print(odds)
            for i in range(m):
                x[i][ind[1]] += 1
                if x[i][ind[1]] % 2 == 0:
                    odds -= 1
                else:
                    odds += 1
                # print(odds)
        return odds
