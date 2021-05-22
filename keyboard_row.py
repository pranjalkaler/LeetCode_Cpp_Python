class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        result = []
        for word in words:
            rows_used = []
            for char in word:
                for i, row in enumerate(rows):
                    if char.lower() in row:
                        rows_used.append(i)
                    # else:
                        # print("searched for {} in {}. rows_used = {}".format(char.lower(), row, rows_used))
            if len(set(rows_used)) == 1:
                result.append(word)
        return result
