class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {}
        
        for e1, e2 in edges:
            parent[e1] = e1
            parent[e2] = e2
        
        def find(node):
            if parent[node] == node:
                return node
            parent[node] = find(parent[node])
            
            return parent[node]
        
        def union(u, v):
            root1, root2 = find(u), find(v)
            
            if root1 != root2:
                parent[root1] = root2
                return []
            else:
                return [u, v]
                
                
        for u, v in edges:
            points = union(u, v)
            if points == [u, v]:
                return points