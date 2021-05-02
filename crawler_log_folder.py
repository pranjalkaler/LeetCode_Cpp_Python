class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for x in logs:
            if x == "../":
                if len(stack) > 0:
                    stack.pop()
            elif x == "./":
                pass
            else:
                stack.append(x)
        return len(stack)
        