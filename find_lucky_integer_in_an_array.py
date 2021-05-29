class Solution:
    def findLucky(self, arr: List[int]) -> int:
        maxKey = -1
        for key, val in Counter(arr).items():
            if key == val and key > maxKey:
                maxKey = key
        return maxKey
