class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        stack = []
        count = 0
        for x in S:
            if x == ")":
                if len(stack) > 0:
                    if stack[-1] == "(":
                        stack.pop()
                    else:
                        count += 1
                else:
                    count += 1
            elif x == "(":
                stack.append(x)
        return count + len(stack)