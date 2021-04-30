class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = [ "" for i in range(len(indices))]
        for i in range(len(indices)):
            result[indices[i]] = s[i]
        res = ""
        for x in result:
            res += x
        return res
        