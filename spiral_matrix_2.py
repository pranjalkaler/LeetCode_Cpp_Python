class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        result = [ [ -1 for i in range(n) ] for i in range(n) ]
        top, bottom, right, left = 0, n, n, -1
        val = 1
        i, j = 0, 0
        # len(result) < n*n
        while True and val <= n*n:
            while j < right:
                # print(f"a {i}, {j} = {val}")
                result[i][j] = val
                val = val + 1
                j = j + 1
            right = right - 1
            j = j - 1
            i = i + 1
            
            while i < bottom:
                # print(f"b {i}, {j} = {val}")
                result[i][j] = val
                val = val + 1
                i = i + 1
            bottom = bottom - 1
            j = j - 1
            i = i - 1
            
            while j > left:
                # print(f"c {i}, {j} = {val}")
                result[i][j] = val
                val = val + 1
                j = j - 1
            left = left + 1
            j = j + 1
            i = i - 1
            
            while i > top:
                # print(f"d {i}, {j} = {val}")
                result[i][j] = val
                val = val + 1
                i = i - 1
            top = top + 1
            j = j + 1
            i = i + 1
        return result
