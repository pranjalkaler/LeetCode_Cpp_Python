class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust:
            return 1 if n == 1 else -1
        t1 = {}
        t2 = {}
        for x in trust:
            t1[x[0]] = t1[x[0]] + 1 if x[0] in t1.keys() else 1
            t2[x[1]] = t2[x[1]] + 1 if x[1] in t2.keys() else 1
        print(t1, t2)
        for x, y in t2.items():
            if y == n - 1:
                if x not in t1.keys():
                    return x
        return -1
