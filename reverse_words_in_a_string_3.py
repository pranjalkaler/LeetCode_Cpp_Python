class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        result = ""
        for word in words:
            result += "{} ".format(word[::-1])
        return result.strip()
