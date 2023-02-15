class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        graph = defaultdict(set)
        visited = set()
        
        for i, num in enumerate(nums):
            for j, num2 in enumerate(nums):
                if i != j:
                    curr = num + num2
                    root = sqrt(curr)
                    if (ceil(root)) ** 2 == curr or floor((root)) ** 2 == curr:
                        graph[num].add((j, num2))
                        graph[num2].add((i, num))
                        
        permutation = 0
        def dfs(node, visited):
            nonlocal permutation
            seenVals = set()
            
            if len(visited) == len(nums):
                permutation += 1
                
            for idx, val in graph[node]:
                if (idx, val) not in visited and val not in seenVals:
                    visited.add((idx, val))
                    seenVals.add(val)
                    dfs(val, visited)
                    visited.remove((idx, val))
                    
        processed = set()
        
        for idx, n in enumerate(nums):
            if n not in processed:
                processed.add(n)
                dfs(n, {(idx, n)})
                
            
        return permutation
                    
                    
            
                
            
                        
                
            
            
                    
                
                
                