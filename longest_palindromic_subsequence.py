class Solution:
    def longestPalindromeSubseq(self, string: str) -> int:
        t = [ [ -1 for i in range(len(string)) ] for j in range(len(string)) ]
        
        def LPS(s, e):
            if s > e:
                return 0
            if t[s][e] != -1:
                return t[s][e]
            else:
                if s == e:
                    t[s][e] = 1
                elif string[s] == string[e]:
                    t[s][e] = 2 + LPS(s+1,e-1)
                else:
                    t[s][e] = max(LPS(s+1,e), LPS(s,e-1))
                return t[s][e]
        
        LPS(0, len(string)-1)
        return t[0][len(string)-1]


#         def LPS(s, e):
#             # print(s, e)
#             if s > e:
#                 return 0
#             if s == e:
#                 return 1
#             else:
#                 if string[s] == string[e]:
#                     return 2 + LPS(s+1, e-1)
#                 else:
#                     return max(LPS(s+1, e), LPS(s, e-1))
        
#         return LPS(0, len(string)-1)
