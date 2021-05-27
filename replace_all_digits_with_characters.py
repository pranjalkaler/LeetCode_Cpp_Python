class Solution:
    def replaceDigits(self, s: str) -> str:
        def shift(ch, x):
            return chr(ord(ch) + x)
        
        result = ""
        for i in range(len(s)):
            if s[i].isnumeric():
                result += (shift(s[i-1], int(s[i])))
            else:
                result += (s[i])
        return result
