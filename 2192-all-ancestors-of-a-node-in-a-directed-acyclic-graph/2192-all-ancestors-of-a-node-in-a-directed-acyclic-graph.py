class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        indegree = {}
        graph = defaultdict(list)
        ans = [ set() for _ in range(n)]
        for i in range(n):
            indegree[i] = 0
            
        for fro , to in edges:
            graph[fro].append(to)
            indegree[to] += 1
             
        queue = deque()
        
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
                
        while queue:
            curr = queue.popleft()
            
            for node in graph[curr]:
                ans[node].add(curr)
                ans[node].update(ans[curr])
                indegree[node] -= 1
                if indegree[node] == 0:
                    queue.append(node)
                    
        return [ sorted(ans[i]) for i in range (n)]
            
        