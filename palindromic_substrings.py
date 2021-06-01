class Solution:
    def countSubstrings(self, s: str) -> int:
        def isPalindrome(string):
            if not string:
                return False
            return string == string[::-1]

        count = 0
        for i in range(len(s)+1):
            for j in range(i, len(s)+1):
                if isPalindrome(s[i:j]):
                    count += 1
        return count
