class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        arr = [-1] * (n + 1)
        arr[0], arr[1], arr[2] = 0, 1, 1
        def fbc(N):
            if arr[N] != -1:
                return arr[N]
            arr[N] = fbc(N-1) + fbc(N-2)
            return arr[N]
        return fbc(n)
