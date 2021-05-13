class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t = list(t)
        s = list(s)
        for x in t:
            print("{}".format(x)*10)
            if not s:
                return True
            if x == s[0]:
                s.pop(0)
        return False if len(s) > 0 else True