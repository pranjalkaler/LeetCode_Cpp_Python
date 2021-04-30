class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for word in words:
            broken = False
            for x in word:
                if x not in allowed:
                    broken = True
            if not broken:
                count += 1
        return count
        