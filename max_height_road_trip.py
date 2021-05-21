class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        height = 0
        maxH = height
        for h in gain:
            height += h
            maxH = max(height, maxH)
        return maxH
