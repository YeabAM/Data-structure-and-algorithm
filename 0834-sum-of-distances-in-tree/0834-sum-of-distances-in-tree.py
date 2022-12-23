class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        
        
        
        graph = defaultdict(list)
        
        ans = [0 for _ in range(n)]
        
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
            
            
        
        @lru_cache(None)
        def num_of_nodes(parent, node):
            #initialize counter
            
            count = 1
            
            
            #go through each neigh which isnt parent
            
            for nei in graph[node]:
                if nei != parent:
                    count += num_of_nodes(node, nei)
            
            
            # //give back counter
            
            return count
            
        @lru_cache(None)    
        def get_distance(parent, node):
            # //initialize distance
            
            distance = 0
            
            # //go thru each neigh which isnt parent
            
            for nei in graph[node]:
                if nei != parent:
                    
                    # //add num_nodes_nodes withh get_distance
                    
                    distance += num_of_nodes(node, nei) + get_distance(node, nei)
                    
                    
            # //give back distance
                    
            return distance
        
        
        for node in range(n):
            ans[node] = get_distance(-1, node)
            
            
        return ans
            
            
                
                
                
            