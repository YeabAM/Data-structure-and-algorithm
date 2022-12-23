class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        rows = len(board)
        cols = len(board[-1])
        count = 0    
        
        in_bound = lambda r, c: 0 <= r < rows and 0 <= c < cols
                        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'X':
                    
                    if (not in_bound(r-1, c) or board[r-1][c] == '.') and\
                    (not in_bound(r, c - 1) or board[r][c - 1] == '.'):
                        
                        count += 1
                    
        return count
                    
        