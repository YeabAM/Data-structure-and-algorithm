class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        
        sorted_query = [[query, i] for i, query in enumerate(queries)]
        sorted_query.sort()
        count = [0 for i in range(len(queries))]
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        visited.add((0, 0))
        heap = [(grid[0][0], 0, 0)]
        in_bound = lambda r, c: 0 <= r < rows and 0 <= c < cols
          
        heapq.heapify(heap)
        points = 0
        direction = [(0, 1),(1, 0),(-1, 0),(0, -1)]
        
        for q, idx in sorted_query:
        
            while heap and heap[0][0] < q:
                points += 1
                
                val, r, c = heapq.heappop(heap)
                
                for dx, dy in direction:
                    nr, nc = r + dx, c + dy
                    
                    if in_bound(nr, nc) and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        heapq.heappush(heap, (grid[nr][nc], nr, nc))
                        
            count[idx] = points
            
        return count
                    
        
        
       