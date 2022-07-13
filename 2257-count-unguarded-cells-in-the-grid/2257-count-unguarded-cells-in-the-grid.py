
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        DIR = [[1,0],[-1,0],[0,1],[0,-1]]
        
        in_bound = lambda row, col : 0 <= row < m and 0 <= col < n
        
        guarded = set()
        
        walls = set([(i, j) for i, j in walls])
        
        guards = set([(i, j) for i, j in guards])
        
        def dfs(row, col, dirX, dirY):
            
            nr = row + dirX
            nc = col + dirY
            
            while (in_bound(nr, nc)):
                if (nr,nc) not in guards and (nr,nc) not in walls:
                    guarded.add((nr,nc))
                    nr = nr + dirX
                    nc = nc + dirY
                    
                else:
                    break
        
        for row, col in guards:
            for dirX, dirY in DIR:
                dfs(row, col, dirX, dirY)
                
        return (m*n - len(guards) - len(walls) - len(guarded))
            
                    
                    