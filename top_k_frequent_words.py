class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        def isGreater(x, y):
            if x[1] > y[1]:
                return True
            elif y[1] > x[1]:
                return False
            if x[1] == y[1]:
                return x[0] < y[0]
            return False

        def insersionSort(arr):
            for i in range(1, len(arr)):
                j = i - 1
                key = arr[i]
                # print("Key = {}".format(key))
                while j >= 0 and isGreater(key, arr[j]):
                    arr[j+1] = arr[j]
                    j = j-1
                arr[j+1] = key
                # print("Updated Array: {}".format(arr))

        freq = {}
        for word in words:
            freq[word] = freq[word] + 1 if word in freq.keys() else 1
        freq = [ (key, val) for key, val in freq.items() ]
        insersionSort(freq)

        result = []
        while k:
            result.append(freq.pop(0)[0])
            k -= 1
        return result
