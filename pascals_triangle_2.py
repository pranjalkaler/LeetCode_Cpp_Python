class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        result = [[1], [1,1]]
        if rowIndex == 1:
            return result[-1]
        result.append([1,2,1])
        if rowIndex == 2:
            return result[-1]

        for i in range(3, rowIndex+1):
            last = result[-1]
            current = [1]
            for k in range(1, len(last)):
                current.append(last[k-1] + last[k])
            current.append(1)
            result.append(current)
        return result[-1]
