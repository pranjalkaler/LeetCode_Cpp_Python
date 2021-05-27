class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        words = s.split(" ")
        result = ""
        for word in reversed(words):
            # print(">{}<".format(word))
            if word:
                result += "{} ".format(word)
        return result.strip()
