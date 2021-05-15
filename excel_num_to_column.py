class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        if columnNumber <= 26:
            return chr(columnNumber + 64)
        last = int(columnNumber % 26) if int(columnNumber % 26) != 0 else 26
        div  = int(columnNumber / 26) if last != 26 else int(columnNumber / 26) - 1
        return "{}{}".format(self.convertToTitle(div), chr(last + 64))