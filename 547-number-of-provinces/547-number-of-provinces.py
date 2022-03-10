class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        count = 0
        queue = deque()
        def bfs(row):
            queue.append(row)
            while queue:
                cur = queue.popleft()
                for col in range(len(isConnected[cur])):
                    if col not in visited and isConnected[cur][col] == 1:
                        visited.add(col)
                        queue.append(col)
                        bfs(col)

            
        
        for row in range(len(isConnected)):
            if row not in visited:
                count += 1
                visited.add(row)
                bfs(row)
        return count
                
       
            
                
        
        
        
        