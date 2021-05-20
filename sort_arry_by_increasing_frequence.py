class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        d1 = {}
        for x in nums:
            d1[x] = d1[x] + 1 if x in d1.keys() else 1
        d2 = {}
        for key, val in d1.items():
            if val in d2.keys():
                d2[val].append(key)
                d2[val].sort(reverse=True)
            else:
                d2[val] = [ key ]
        result = []
        for x in sorted(d2.keys()):
            for y in d2[x]:
                result.extend([y] * x)
        return result