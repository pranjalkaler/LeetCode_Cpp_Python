class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        top_lim, rig_lim, lef_lim, bot_lim = 0, m, -1, n
        
        result = list()
        i, j = 0, 0
        while True and len(result) < n*m:
            while j < rig_lim:
                # print(f"a {i}, {j}")
                result.append(matrix[i][j])
                j = j + 1
            rig_lim = rig_lim - 1
            j = j - 1
            i = i + 1
            if len(result) == n*m:
                break
            while i < bot_lim:
                # print(f"b {i}, {j}")
                result.append(matrix[i][j])
                i = i + 1
            bot_lim = bot_lim - 1
            i = i - 1
            j = j - 1
            if len(result) == n*m:
                break
            while j > lef_lim:
                # print(f"c {i}, {j}")
                result.append(matrix[i][j])
                j = j - 1
            lef_lim = lef_lim + 1
            j = j + 1
            i = i - 1
            if len(result) == n*m:
                break
            while i > top_lim:
                # print(f"d {i}, {j}")
                result.append(matrix[i][j])
                i = i - 1
            top_lim = top_lim + 1
            i = i + 1
            j = j + 1
            if len(result) == n*m:
                break
        return result
