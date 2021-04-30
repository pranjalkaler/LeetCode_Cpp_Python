class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        maxDep = 0
        for x in s:
            if x == "(":
                depth = depth + 1
            if x == ")":
                depth = depth - 1
            maxDep = depth if maxDep <= depth else maxDep
        return maxDep
                