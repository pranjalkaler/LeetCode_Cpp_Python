class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for x in s:
            if len(stack) > 0:
                if x.isupper() and stack[-1] == x.lower()\
                or x.islower() and stack[-1] == x.upper():
                    stack.pop()
                else:
                    stack.append(x)
            else:
                stack.append(x)
        return "".join(stack)