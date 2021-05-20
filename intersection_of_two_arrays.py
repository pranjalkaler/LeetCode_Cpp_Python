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
        return resultclass Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        p1 = 0
        p2 = 0
        result = []
        print(nums1, nums2)
        while p1 <= len(nums1) - 1 and p2 <= len(nums2) - 1:
            print(p1, p2, nums1[p1], nums2[p2])
            if nums1[p1] == nums2[p2]:
                result.append(nums1[p1])
                p1 += 1
                p2 += 1
            elif nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                p2 += 1
        result1 = []
        for x in set(result):
            result1.append(x)
        return result1