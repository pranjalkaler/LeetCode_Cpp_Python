class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        w1 = ""
        w2 = ""
        for x in word1:
            w1 += x
        for x in word2:
            w2 += x
        return w1 == w2
        