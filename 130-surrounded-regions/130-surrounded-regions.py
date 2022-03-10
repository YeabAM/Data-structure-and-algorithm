class Solution:
    def solve(self, board: List[List[str]]) -> None:
        DIR = [[1,0], [0,1],[-1,0],[0,-1]]
        in_bound = lambda row, col : 0 <= row < len(board) and 0 <= col < len(board[0])
        visited = set((0, 0))
        r = len(board)
        c = len(board[0])
        
        def dfs(row, col):
            visited.add((row, col))
            for direction in DIR:
                newRow, newCol = row + direction[0], col + direction[1]
                if (newRow, newCol) not in visited and \
                in_bound(newRow, newCol) \
                and board[newRow][newCol] != "X":
                    dfs(newRow, newCol)
        
        for i in range(r):
            for j in range(c):
                if i == 0 or j == 0 or i == r -1 or j == c - 1:
                    if (i, j) not in visited and board[i][j] == "O":
                        dfs(i, j)                 
        for i in range(r):
            for j in range(c):
                if (i, j) not in visited and board[i][j] == "O":
                    board[i][j] = "X"
        
        
        
        