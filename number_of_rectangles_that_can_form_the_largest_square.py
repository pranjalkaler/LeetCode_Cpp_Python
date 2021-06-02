class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        freq = {}
        for i in range(len(rectangles)):
            rectangles[i] = min(rectangles[i][0], rectangles[i][1])
            freq[rectangles[i]] = freq[rectangles[i]] + 1 if rectangles[i] in freq.keys() else 1
        return freq[max(freq.keys())]
