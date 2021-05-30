class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_dis = 1000000
        pos = -1

        get_distance = lambda point : abs(point[0] - x) + abs(point[1] - y)

        for i, point in enumerate(points):
            if point[0] == x or point[1] == y:
                dis = get_distance(point)
                if dis < min_dis:
                    min_dis = dis
                    pos = i
        return pos
