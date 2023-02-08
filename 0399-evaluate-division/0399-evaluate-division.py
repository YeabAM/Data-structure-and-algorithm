class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        
        
        for i in range(len(values)):
            val = values[i]
            u, v = equations[i]
            graph[u].append((v, val))
            if val > 0:
                graph[v].append((u, 1/val))
                
        
        
        def bfs(u, v):
            queue = deque()
            visited.add(u)
            dest = v
            queue.append((u,1))
            
            while queue:
                curr, quot = queue.popleft()
                
                if len(graph[curr]) == 0:
                    return -1
                
                if curr == dest:
                    return quot
                
                for nei, val in graph[curr]:
                    if nei not in visited:  
                        queue.append((nei, quot*val))
                        visited.add(nei)
                        
            return -1
        
        ans = []
        for query in queries:
            u, v = query
            visited = set()
            ans.append(bfs(u, v))
            
        return ans
        
        
        
                    
            
                    
        