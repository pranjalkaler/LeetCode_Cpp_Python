class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        caps = 0
        for x in word:
            if x.isupper():
                caps += 1
        if not caps or len(word) == caps:
            return True
        if caps == 1 and word[0].isupper():
            return True
        return False
