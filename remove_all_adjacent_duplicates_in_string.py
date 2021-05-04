class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        counter = 0
        for x in s:
            if len(stack) == 0:
                counter += 1
                dct = [ x , counter ]
                stack.append(dct)
            else:
                if x == stack[-1][0]:
                    counter += 1
                    stack[-1][1] = counter
                    if counter == k:
                        stack.pop()
                        counter = stack[-1][1] if len(stack) > 0 else 0
                else:
                    counter = 1
                    dct = [x, counter]
                    stack.append(dct)
        result = ""
        for x in stack:
            result += x[0]*x[1]
        return result
        