class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 2:
            return 1
        arr = [-1] * (n + 1)
        arr[0], arr[1], arr[2] = 0, 1, 1
        def tbc(N):
            print(N)
            if arr[N] != -1:
                return arr[N]
            arr[N] = tbc(N-1) + tbc(N-2) + tbc(N-3)
            return arr[N]
        return tbc(n)
