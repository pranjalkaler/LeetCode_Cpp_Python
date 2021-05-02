class Solution:
    def calPoints(self, ops: List[str]) -> int:
        score = []
        for x in ops:
            if x == "C":
                score.pop()
            elif x == "D":
                score.append(score[-1]*2)
            elif x == "+":
                score.append(score[-1] + score[-2])
            else:
                score.append(int(x))
            print(score)
        return sum( [int(x) for x in score] )
        