class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        words = s.split(" ")
        print(words)
        if len(words) == 0:
            return 0
        return len(words[-1])
