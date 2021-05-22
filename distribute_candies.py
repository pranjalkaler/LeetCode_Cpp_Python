class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        Hash = {}
        for x in candyType:
            if x not in Hash.keys():
                Hash[x] = 1
        return min(len(Hash), int(len(candyType)/2))
