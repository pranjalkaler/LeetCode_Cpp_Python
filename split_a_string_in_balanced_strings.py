class Solution:
    def balancedStringSplit(self, s: str) -> int:
        if len(s) == 1:
            return 0
        stack = []
        count = 0
        s = list(s)
        while s:
            ch = s.pop(0)
            if not stack:
                stack.append(ch)
            else:
                if stack[-1] == ch:
                    stack.append(ch)
                else:
                    stack.pop()
                    if not stack:
                        count += 1
        return count
