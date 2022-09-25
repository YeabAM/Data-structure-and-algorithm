class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        parents = [-1 for _ in range(n)]
        
        def find(node):
            
            while parents[node] > 0:
                node = parents[node]
            
            return node
        
        def union(u, v):
            pu = find(u)
            pv = find(v)
            
            if pu != pv and pu != -1 and pv != -1:

                if parents[pu] < parents[pv]:
                    parents[pu] += parents[pv]
                    parents[pv] = pu

                else:
                    parents[pv] += parents[pu]
                    parents[pu] = pv
                
                
        
        for u, v in edges:
            union(u, v)
            
        print(parents)
        return find(source) == find(destination)
        