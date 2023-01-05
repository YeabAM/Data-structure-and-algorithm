class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        if not edges:
            return max(vals)
        
        graph = defaultdict(list)
        
        for edg1, edg2 in edges:
            graph[edg1].append([vals[edg2],edg2])
            graph[edg2].append([vals[edg1],edg1])
        
            
        for node in graph:
            temp = sorted(graph[node], reverse = True)
            graph[node] = temp
            
        max_sum = float('-inf')
        
        for node in graph: 
            i = 0
            curr_sum = vals[node]
            while i < k and i < len(graph[node]):
                if graph[node][i][0] < 0:
                    break
                curr_sum += graph[node][i][0]
                i += 1
            # print(node, curr_sum)
            max_sum = max(max_sum, vals[node], curr_sum)
            
        val_max = max(vals)
        
        return max(max_sum, val_max)
    
            
        