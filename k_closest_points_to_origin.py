class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if len(points) == 1:
            return points

        distance = lambda point : point[0] ** 2 + point[1] ** 2
        points.sort(key=distance)
        print(points)
        return points[0:k]
