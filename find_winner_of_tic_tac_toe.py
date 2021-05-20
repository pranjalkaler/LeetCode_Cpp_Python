class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        if len(moves) < 5:
            return "Pending"
        def isGameOver(grid):
            for i in range(3):
                if grid[i][0] == grid[i][1] and grid[i][1] == grid[i][2] and grid[i][2] != ' ':
                    return True
                if grid[0][i] == grid[1][i] and grid[1][i] == grid[2][i] and grid[0][i] != ' ':
                    return True
            if ((grid[0][0] == grid[1][1] and grid[1][1] == grid[2][2]) or\
               (grid[0][2] == grid[1][1] and grid[1][1] == grid[2][0])) and grid[1][1] != ' ':
                print(3)
                return True
            return False
                
        grid = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
        ]
        turn_of_A= True
        for move in moves:
            char = 'X' if turn_of_A else 'O'
            grid[move[0]][move[1]] = char
            if isGameOver(grid):
                return "A" if turn_of_A else "B"
            turn_of_A = not turn_of_A
        if len(moves) < 9:
            return "Pending"
        return "Draw"