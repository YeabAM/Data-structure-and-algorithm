class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        DIR = [(0,1),(1,0),(0,-1),(-1,0)]
        in_bound = lambda row, col : 0 <= row < len(grid) and 0 <= col < len(grid[0])
        visited = set()
        q = deque()
        self.minute = 0
        count = 0
            
            
            
        
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    count += 1
                
        
        while q:
            size = len(q)
            check = False
            for _ in range(size):
                rw, cl = q.popleft()
                for direction in DIR:
                    newRow, newCol = rw + direction[0], cl + direction[1]
                    if in_bound(newRow, newCol) and grid[newRow][newCol] == 1:
                        count -= 1
                        grid[newRow][newCol] = 2
                        check = True
                        q.append((newRow, newCol))
            if check:
                self.minute += 1
                        
        print(self.minute)   
        if count != 0:
            return -1 
        return self.minute
                
                
                    