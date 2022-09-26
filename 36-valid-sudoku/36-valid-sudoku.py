class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def buildRow(i, j):
            row = set()
            
            for k in range(9):
                if k != j:
                    row.add(board[i][k])
            
            return board[i][j] in row
        
        def buildCol(i, j):
            col = set()
            
            for k in range(9):
                if k != i:
                    col.add(board[k][j])
                    
            return board[i][j] in col
                    
        def buildBox(i, j):
            box = set()
            Rlimit = (i // 3) * 3
            Climit = (j // 3 ) * 3

            for r in range(Rlimit, Rlimit + 3):
                for c in range(Climit, Climit + 3):
                    # print(r, c,i,j, r != i , c != j)
                    if r != i or c != j:
                        # print(r,c, "in")
                        box.add(board[r][c])
                        
            return board[i][j] in box
                        
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if buildRow(i,j) or buildCol(i,j) or buildBox(i,j):
                        return False
        
        return True
                    
                
            
            
        