class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        Sum = sum(nums)
        if Sum % 2 != 0:
            return False
        
        req = int(Sum / 2)
        t = [[-1 for i in range(len(nums)+1)] for j in range(req + 1)]
        def KS(n, s):
            if n == 0:
                if t[s][n] == -1:
                    t[s][n] = 0
                return False
            if t[s][n] != -1:
                return t[s][n]
            if s - nums[n-1] == 0:
                t[s][n] = 1
                return True
            v1 = 1 if KS(n-1, s) else 0
            v2 = 1 if KS(n-1, s-nums[n-1]) else 0
            t[s][n] = max(v1, v2)
            return True if v1 == 1 or v2 == 1 else 0
        
        return KS(len(nums), req)
