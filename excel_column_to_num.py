class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        if len(columnTitle) == 1:
            return ord(columnTitle) - 64
        return self.titleToNumber(columnTitle[:-1])*26 + ord(columnTitle[-1]) - 64