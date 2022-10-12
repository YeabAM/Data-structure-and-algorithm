class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        parent = {}
        rank = [1 for _ in range(len(graph))]
        
        for i in range(len(graph)):
            parent[i] = i
            
        
        def find(node):
            if parent[node] == node:
                return node
            parent[node] = find(parent[node])
            
            return parent[node]
        
        def union(u, v):
            p1, p2 = find(u), find(v)
            
            if p1 != p2:
                if rank[p1] < rank[p2]:
                    p1, p2 = p2, p1
                    
                if rank[p1] == rank[p2]:
                    rank[p1] += 1
                    
                parent[p2] = p1
                
        for j in range(len(graph)):
            edges = graph[j]
            for i in range(1, len(edges)):
                if find(edges[i]) == find(j):
                    return False
                union(edges[0], edges[i])
                
        return True
                
                
        
                
                    
        