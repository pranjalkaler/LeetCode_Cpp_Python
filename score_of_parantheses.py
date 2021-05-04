class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = []
        for x in S:
            if x == ")":
                number = 0
                while stack[-1] != "(":
                    number += int(stack.pop())
                stack.pop()
                if number == 0:
                    stack.append("1")
                else:
                    stack.append(str(number * 2))
                
            else:
                stack.append(x)
        print(stack)
        result = 0
        for x in stack:
            result += int(x)
        return result