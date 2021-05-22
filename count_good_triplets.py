class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        i , j, k = 0, 1, 2
        size = len(arr)
        count = 0
        while i < size - 2:
            j = i + 1
            while j < size - 1:
                k = j + 1
                while k < size:
                    if abs(arr[i] - arr[j]) <= a and\
                       abs(arr[j] - arr[k]) <= b and\
                       abs(arr[i] - arr[k]) <= c:
                        count += 1
                    k += 1
                j += 1
            i += 1
        return count