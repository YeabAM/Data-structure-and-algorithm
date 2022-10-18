class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        col = 0
        row = 0
        col_change = 1
        row_change = 0
        in_bound = lambda r,c: 0 <= r < n and 0 <= c < n
        
        for i in range(n*n):
            matrix[row][col] = i + 1
            new_row = row+row_change
            new_col = col+col_change
            if not in_bound(new_row,new_col) or matrix[row+row_change][col+col_change] != 0:
                col_change, row_change = -row_change, col_change
            col, row = col + col_change, row + row_change
            
        return matrix