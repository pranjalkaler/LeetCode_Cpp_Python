class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        def distance(p1, p2):
            return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
        
        result = list()
        for query in queries:
            count = 0
            center = [query[0], query[1]]
            radius = query[2]
            for point in points:
                dist = distance(center, point)
                # print(f"Distance between {point} and {center} is {dist}")
                if dist <= radius:
                    count = count + 1
            result.append(count)
        return result
