class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        newStack = []
        for idx, x in enumerate(pushed):
            if x != popped[0]:
                newStack.append(x)
            else:
                del popped[0]
                print(popped)
                while len(popped) > 0 and len(newStack) > 0 and newStack[-1] == popped[0]:
                    del popped[0]
                    newStack.pop()
            
        while len(popped) > 0 and popped[0] == newStack[-1]:
            del popped[0]
            newStack.pop()
        return False if len(popped) > 0 else True