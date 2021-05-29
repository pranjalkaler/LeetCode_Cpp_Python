class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split(" ")
        maxL = max([len(x) for x in words])
        # print(maxL)
        Words = [ [ char for char in word] for word in words]
        # print(Words)
        result = []
        for i in range(maxL): # 0, 1, 2
            col = []
            for j in range(len(Words)): # 0, 1, 2, 3, 4, 5
                if len(Words[j]) <= i:
                    char = ' '
                else:
                    char = Words[j][i]
                # print(col)
                col.append(char)
            result.append("".join(col).rstrip())
        return result
