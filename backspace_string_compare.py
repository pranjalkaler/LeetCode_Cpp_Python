class Solution:
    def getStr(self, s):
        arr = []
        for x in s:
            if x == "#":
                if len(arr) > 0:
                    arr.pop()
            else:
                arr.append(x)
        return "".join(arr)

                
    def backspaceCompare(self, s: str, t: str) -> bool:
        str1, str2 = self.getStr(s), self.getStr(t)
        return str1 == str2