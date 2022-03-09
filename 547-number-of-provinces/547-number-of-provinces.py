class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        n = len(isConnected)
        que = deque()
        def bfs(row):
            que.append(row)
            while que:
                cur = que.popleft()
                for col in range(n):
                    if isConnected[cur][col] == 1 and col not in visited:
                        visited.add(col)
                        que.append(col)
           
        count = 0
        for i in range(n):
            if i not in visited:
                count += 1
                visited.add(i)
                bfs(i)
        return count
            
                
        
        
        
        