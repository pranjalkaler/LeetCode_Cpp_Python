class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        freq1 = { x : 0 for x in range(1, max(arr) + 1)}
        freq2 = { x : 0 for x in range(1, max(target) + 1)}
        for x in arr:
            freq1[x] += 1
        for x in target:
            freq2[x] += 1
        for i in freq1.keys():
            if freq2[i] != freq1[i]:
                return False
        return True