class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(" ")
        print(len(words))
        Dict = {}
        for word in words:
            Dict[int(word[-1])] = word[:-1]
        result = ""
        for i in range(1, len(words)+1):
            result += "{} ".format(Dict[i])
        return result[:-1]