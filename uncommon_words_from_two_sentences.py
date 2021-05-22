class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        Hash = {}
        def updateHash(s):
            for x in s:
                Hash[x] = Hash[x] + 1 if x in Hash.keys() else 1
        
        updateHash(s1.split(" "))
        updateHash(s2.split(" "))
        result = []
        for idx, val in Hash.items():
            if val == 1:
                result.append(idx)
        return result
