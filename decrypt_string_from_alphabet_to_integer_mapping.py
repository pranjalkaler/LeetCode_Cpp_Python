class Solution:
    def freqAlphabets(self, s: str) -> str:
        stack = list(s)
        result = ""
        while stack:
            char = stack.pop()
            if char == '#':
                zeroth = int(stack.pop())
                ones = int(stack.pop())
                num = ones*10 + zeroth
            else:
                num = int(char)
            # print(num)
            result += chr(num+96)
        # print(result)
        return result[::-1]
