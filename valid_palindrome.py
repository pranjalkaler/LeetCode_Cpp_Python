class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [ x for x in s if x.isalnum()]
        for i in range(len(s)):
            if s[i].isalpha():
                s[i] = s[i].lower()
        s = "".join(s)
        return s == s[::-1]
