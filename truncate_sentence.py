class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        words = s.split(" ")
        result = ""
        for i in range(k):
            result += "{} ".format(words[i])
        return result.strip()
