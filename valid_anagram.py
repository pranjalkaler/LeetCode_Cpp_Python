class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dcx = {}
        for char in s:
            dcx[char] = dcx[char] + 1 if char in dcx.keys() else 1
        # print(dcx)
        for char in t:
            if char not in dcx.keys():
                return False
            dcx[char] -= 1
            if dcx[char] == 0:
                del dcx[char]
        # print(dcx)
        return not dcx
