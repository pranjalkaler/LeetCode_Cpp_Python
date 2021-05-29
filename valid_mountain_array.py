class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) <= 2:
            return False
        
        uphill = 0
        for i in range(1, len(arr)):
            if arr[i] == arr[i-1]:
                # plateau
                return False
            if arr[i] > arr[i-1]:
                uphill += 1
            if arr[i] < arr[i-1]:
                # arr[i-1] is first peak
                break
        peak = i-1
        downhill = 0
        for i in range(peak+1, len(arr)):
            if arr[i] == arr[i-1]:
                # plateau
                return False
            if arr[i] < arr[i-1]:
                downhill += 1
            if arr[i] > arr[i-1]:
                # arr[i-1] is second peak
                return False
        if not uphill or not downhill:
            return False
        return True
