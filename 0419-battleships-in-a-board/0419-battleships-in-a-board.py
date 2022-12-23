class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        rows = len(board)
        cols = len(board[-1])
        
        
        visited = set()
        count = 0
        direction = [(0, 1), (0, -1),(1, 0),(-1, 0)]
        in_bound = lambda r, c: 0 <= r < rows and 0 <= c < cols
        
        def bfs(r, c):
            
            queue = deque()
            queue.append((r, c))
            visited.add((r, c))
            
            while queue:
                r, c = queue.popleft()
            
                for dx, dy in direction:
                    nr, nc = r + dx, c + dy

                    if in_bound(nr, nc) and (nr, nc) not in visited and board[nr][nc] == 'X':
                        visited.add((nr, nc))
                        queue.append((nr, nc))
                        
                        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'X' and (r, c) not in visited:
                    bfs(r, c)
                    count += 1
                    
        return count
                    
        