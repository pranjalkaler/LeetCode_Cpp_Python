class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        size = len(T)
        stack = [size - 1]
        nexyDay = [ 0 for x in range(size) ]
        for i in range(size - 2, -1, -1): # start, stop, step
            if T[i] < T[stack[-1]]:
                nexyDay[i] = stack[-1] - i
            else:
                while len(stack) > 0 and T[i] >= T[stack[-1]]:
                    stack.pop()
                if len(stack) != 0:
                    nexyDay[i] = stack[-1] - i
            stack.append(i)
        print(nexyDay)
        
        return nexyDay
