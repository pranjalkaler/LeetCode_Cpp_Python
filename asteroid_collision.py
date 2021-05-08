class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for x in asteroids:
            if x > 0:
                stack.append(x)
            else:
                if not stack:
                    stack.append(x)
                elif stack and stack[-1] < 0:
                    stack.append(x)
                elif stack and stack[-1] > 0:
                    # collision
                    while x and stack and stack[-1] > 0:
                        if abs(x) > abs(stack[-1]):
                            stack.pop()
                        elif abs(x) < abs(stack[-1]):
                            x = 0
                        elif x == -stack[-1]:
                            stack.pop()
                            x = 0
                    if ( not stack or x ) and x != 0:
                        stack.append(x)
        return stack