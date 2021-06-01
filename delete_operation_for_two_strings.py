class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        t = [ [ -1 for i in range(len(word2) + 1)] for j in range(len(word1) + 1)]

        def LCS(i, j):
            if i == 0 or j == 0:
                if t[i][j] == -1:
                    t[i][j] = 0
                t[i][j] == 0
            if t[i][j] != -1:
                return t[i][j]
            else:
                if word1[i-1] == word2[j-1]:
                    t[i][j] = 1 + LCS(i-1, j-1)
                else:
                    t[i][j] = max(LCS(i-1, j), LCS(i, j-1))
            return t[i][j]
        
        lcs = LCS(len(word1), len(word2))
        return (len(word1) - lcs) + (len(word2) - lcs)
