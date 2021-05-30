class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for x in nums:
            freq[x] = freq[x] + 1 if x in freq.keys() else 1
        freq = [ (key, val) for key, val in freq.items() ]
        freq.sort(reverse=True, key=lambda x : x[1])
        print(freq)
        result = []
        while k:
            result.append(freq.pop(0)[0])
            k -= 1
        return result
