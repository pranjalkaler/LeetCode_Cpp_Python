class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        def is_palin(string):
            return string and string == string[::-1]
        
        longest = ""
        size = 0
        for i in range(len(s)+1):
            for j in reversed(range(i, len(s)+1)):
                if is_palin(s[i:j]) and len(s[i:j]) > size:
                    size = len(s[i:j])
                    longest = s[i:j]
        return longest
