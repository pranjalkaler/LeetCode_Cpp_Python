class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        t = [ [ -1 for i in range(len(text2) + 1) ] for j in range(len(text1) + 1) ]
        def LCS(i, j):
            if i == 0 or j == 0:
                if t[i][j] == -1:
                    t[i][j] = 0
                return t[i][j]
            if t[i][j] != -1:
                return t[i][j]
            else:
                if text1[i-1] == text2[j-1]:
                    t[i][j] = 1 + LCS(i-1, j-1)
                else:
                    t[i][j] = max(LCS(i-1,j), LCS(i, j-1))
                return t[i][j]

        result = LCS(len(text1), len(text2))
        return result
