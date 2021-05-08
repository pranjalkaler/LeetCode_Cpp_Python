class Solution:
    def operate(self, num1, num2, op):
        if op == "+":
            return num1 + num2
        if op == "-":
            return num1 - num2
        if op == "*":
            return num1 * num2
        return int(num1 / num2)

    def evalRPN(self, tokens: List[str]) -> int:
        operations = { "+", "-", "*", "/"}
        stack = []
        for x in tokens:
            if x not in operations:
                stack.append(x)
            else:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                stack.append(self.operate(num1, num2, x))
        print(stack)
        return stack[0]