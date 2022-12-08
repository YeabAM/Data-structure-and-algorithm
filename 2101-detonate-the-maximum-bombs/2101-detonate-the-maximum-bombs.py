class Solution:
    def radius(self, x1, y1, x2, y2):
        xdif = (abs(x1 - x2)) ** 2
        ydif = abs(y1 - y2) ** 2
        
        return sqrt((xdif + ydif))
    
        
    def explode(self, visited, start, graph):
        
        queue = deque()
        queue.append(start)
        
        while queue:
            pos = queue.popleft()
            for bomb in graph[pos]:
                if bomb not in visited:
                    queue.append(bomb)
                    visited.add(bomb)
        
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        maxCount = 0
        
        graph = defaultdict(list)
        
        for idx,(x, y, r) in enumerate(bombs):
            for j, (jx,jy,jr) in enumerate(bombs):
                if self.radius(x, y, jx, jy) <= r:
                    graph[idx].append(j)
                    
        
        
        for i in range(len(bombs)):
            visited = set()
            visited.add(i)
            
            self.explode(visited, i, graph)
            
            maxCount = max(maxCount, len(visited))
                
        return maxCount
                
        
        
        
        
        