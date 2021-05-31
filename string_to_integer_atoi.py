class Solution:
    def myAtoi(self, s: str) -> int:
        integer = 0
        s = list(s.strip())
        if not s:
            return 0
        positive = True
        if s[0] == '-' or s[0] == '+':
            positive = False if s[0] == '-' else True
            s.pop(0)
        if s and s[0].isnumeric():
            while s and s[0].isnumeric():
                integer *= 10
                integer += ord(s.pop(0)) - 48
            if integer >= 2 ** 31:
                integer = 2 ** 31
                integer = integer - 1 if positive else integer
            return integer if positive else integer*-1
        return integer
