class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        Hash = {}
        for x in list(text):
            Hash[x] = Hash[x] + 1 if x in Hash.keys() else 1
        minMap1 = ['b', 'a', 'n']
        minMap2 = ['l', 'o']
        count1 = 100000000
        for x in minMap1:
            if x not in Hash.keys():
                return 0
            freq = Hash[x]
            if freq < count1:
                count1 = freq
        print(count1)
        count2 = 100000000
        for x in minMap2:
            if x not in Hash.keys():
                return 0
            freq = Hash[x]
            if freq < count2:
                count2 = freq
        print(count2)
        return min(count1, int(count2/2))
