class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        def is_palin(i, j, diff):
            if i > j:
                return False
            if i == j:
                return True
            if s[i] == s[j]:
                if i+1 <= j-1:
                    return is_palin(i+1, j-1, diff)
                else:
                    return True
            else:
                diff -= 1
                if diff:
                    left = is_palin(i+1, j, diff)
                    right = is_palin(i, j-1, diff)
                    return left or right
            return False
        return is_palin(0, len(s)-1, 2)
        # t = [[-1 for i in range(len(s))] for j in range(len(s))]
        # def LCP(i, j):
        #     if i > j:
        #         return 0
        #     if t[i][j] != -1:
        #         return t[i][j]
        #     else:
        #         if i == j:
        #             t[i][j] = 1
        #         elif s[i] == s[j]:
        #             t[i][j] = LCP(i+1, j-1) + 2
        #         else:
        #             t[i][j] = max(LCP(i+1, j), LCP(i, j-1))
        #     return t[i][j]
        # LCP(0, len(s)-1)
        # return abs(t[0][len(s) - 1] - len(s)) <= 1
