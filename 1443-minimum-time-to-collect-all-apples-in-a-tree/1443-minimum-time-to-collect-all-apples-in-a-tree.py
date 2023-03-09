class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        if not edges:
            return 0
        graph = defaultdict(list)
        
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)
            
        def dfs(parent, node):
            if not graph[node]:
                return hasApple[node]
            
            currVariable = 0
            # print(node, currVariable, "before")
            for nei in graph[node]:
                if nei != parent:
                    currVariable += dfs(node, nei)
                
            
            if (currVariable > 0 or hasApple[node]) and node != 0:
                currVariable += 1
                
            # print(node, currVariable, 'after')
        
                    
            return currVariable
        
        
        total_variable = dfs(-1, 0)
        # print(total_variable)
        
        return total_variable * 2