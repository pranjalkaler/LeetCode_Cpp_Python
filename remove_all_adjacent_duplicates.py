class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for x in S:
            if len(stack) > 0:
                if stack[-1] == x:
                    stack.pop()
                else:
                    stack.append(x)
            else:
                stack.append(x)
        return "".join(stack)