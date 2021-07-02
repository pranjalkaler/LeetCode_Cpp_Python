class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        if numRows == 1:
            return result
        result.append([1,1])
        if numRows == 2:
            return result
        result.append([1,2,1])

        for i in range(3, numRows):
            last = result[-1]
            current = [1]
            for k in range(1, len(last)):
                current.append(last[k-1] + last[k])
            current.append(1)
            result.append(current)
        return result
