class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for idx, val in enumerate(arr[:len(arr) - 1]):
            arr[idx] = max(arr[idx+1:])
        arr[len(arr) - 1] = -1
        return arr