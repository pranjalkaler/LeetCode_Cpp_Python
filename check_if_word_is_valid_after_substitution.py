class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 3:
            return False
        stack = [""]
        current = stack[-1]
        for x in s:
            if current == "" and x == "a":
                current = x
            elif current == "a" and x == "b":
                current += x
            elif current == "ab" and x == "c":
                if len(stack) > 1:
                    current = stack.pop()
                else:
                    current = ""
            else:
                if current != "":
                    stack.append(current)
                current = x
        print(stack)
        if current != "":
            return False
        return len(stack) == 1
        