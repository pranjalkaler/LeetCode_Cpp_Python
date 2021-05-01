class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = len(s)
        for x in range(int(l/2)):
            temp = s[x]
            s[x] = s[l - x - 1]
            s[l - x - 1] = temp
        