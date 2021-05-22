class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        Hash = {}
        for x in s:
            Hash[x] = Hash[x] + 1 if x in Hash.keys() else 1
        for x in t:
            if x not in Hash.keys():
                return x
            Hash[x] -= 1
            if Hash[x] == 0:
                del Hash[x]