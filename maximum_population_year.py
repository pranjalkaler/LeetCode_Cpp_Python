class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        years = [ 0 ] * 101
        for log in logs:
            for year in range(log[0], log[1]):
                years[year - 1950] += 1
                # print("Updating {} from {} to {}".format(year - 1950, years[year - 1950] - 1, years[year - 1950]))
        maX = 0
        for x in range(1, len(years)):
            if years[x] > years[maX]:
                maX = x
        return maX + 1950