class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = arr[1] - arr[0]
        for x in range(2, len(arr)):
            if arr[x] - arr[x - 1] != diff:
                return False
        return True
            