class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        # ( a * b) % c = ( ( a % c ) * ( b % c ) ) % c
        maxH = 0
        horizontalCuts.append(h)
        horizontalCuts.insert(0, 0)
        horizontalCuts.sort()
        
        maxV = 0
        verticalCuts.append(w)
        verticalCuts.insert(0, 0)
        verticalCuts.sort()
        
        for i in range(1, len(horizontalCuts)):
            if horizontalCuts[i] - horizontalCuts[i-1] > maxH:
                maxH = horizontalCuts[i] - horizontalCuts[i-1]
        
        for i in range(1, len(verticalCuts)):
            if verticalCuts[i] - verticalCuts[i-1] > maxV:
                maxV = verticalCuts[i] - verticalCuts[i-1]
        area = ( ( maxH % 1000000007 ) * ( maxV % 1000000007 ) % 1000000007 )
        return area
