class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        for u, v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)
            
        queue = deque()
        
        for num in graph:
            if len(graph[num]) == 1:
                queue.append((num, 110000))
                break
        original_nums = []  
        
        while queue:
            curr, parent = queue.popleft()
            original_nums.append(curr)
            
            for adj in graph[curr]:
                if adj != parent:
                    queue.append((adj, curr))
                    
        return original_nums
                
        
        