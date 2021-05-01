class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sortd = [x for x in heights]
        sortd.sort()
        count = 0
        for (x, y) in zip(sortd, heights):
            print(x, y)
            if x != y:
                count += 1
        return count