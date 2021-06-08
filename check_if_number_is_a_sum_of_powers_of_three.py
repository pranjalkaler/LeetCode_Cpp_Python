class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        arr = []
        i = 0
        while 3 ** i <= n:
            arr.append(3 ** i)
            i += 1
        print(arr)
        def KS(size, _sum):
            print(size, _sum)
            if _sum == 0:
                return True
            if size <= 0 or _sum < 0:
                return False
            return KS(size - 1, _sum - arr[size-1]) or KS(size - 1, _sum)
        
        return KS(len(arr), n)
