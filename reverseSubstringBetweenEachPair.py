class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        charstack = []
        curr_word = []
        for x in s:
            if x == ")":
                while charstack[-1] != "(":
                    curr_word.append(charstack.pop())
                    print("curr_word = ", curr_word)
                charstack.pop()
                charstack.extend(curr_word)
                curr_word = []
            else:
                charstack.append(x)
        print("stack: {}, charstack: {}, curr_word: {}".format(stack, charstack, curr_word))
        return "".join(charstack)