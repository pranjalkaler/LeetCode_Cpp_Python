class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        luckyNumbers = []
        for idx, row in enumerate(matrix):
            minrowpos = row.index(min(row))
            column = [matrix[x][minrowpos] for x in range(len(matrix))]
            maxcolpos = column.index(max(column))
            if maxcolpos == idx:
                luckyNumbers.append(matrix[maxcolpos][minrowpos])
        return luckyNumbers
