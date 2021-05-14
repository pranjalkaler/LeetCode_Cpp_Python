class Solution:
    def maximum69Number (self, num: int) -> int:
        chars = list(str(num))
        flag = False
        for i, x in enumerate(chars):
            if x == '6':
                flag = True
                break
        if flag:
            chars[i] = '9'
        return int("".join(chars))