class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        global_count = [1 for _ in range(n)]
        
        graph = defaultdict(list)
        
        
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)
        
        def dfs(parent, node):
            counter = defaultdict(int)
            total = 0
            
            for nei in graph[node]:
                if nei != parent:
                    curr = dfs(node, nei)
                    curr[labels[nei]] += 1
                    total += curr[labels[node]]
                    
                    for i in curr:
                        counter[i] += curr[i]
                    

            global_count[node] += total
            
            return counter
        
        dfs(-1, 0)
        
        return global_count
                    
            
                    
            
            
                
                
            