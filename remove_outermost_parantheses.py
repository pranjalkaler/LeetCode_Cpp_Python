class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        size, stack, result = 0, [], ""
        opening = closing = -1
        for idx, val in enumerate(S):
            if val == "(":
                if len(stack) == 0:
                    # this is an opening tag
                    opening = idx
                stack.append(val)
            elif val == ")":
                stack.pop()
                if len(stack) == 0:
                    # this was a closing tag
                    closing = idx
            if opening < closing and opening > -1 and closing > -1:
                # we have found an outer layer
                result += S[opening + 1: closing]
                opening = closing = -1
        return result