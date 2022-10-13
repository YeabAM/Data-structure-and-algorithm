class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) <= 1:
            return len(nums)
        
        parent = {}
        count = defaultdict(int)
        
        for num in nums:
            parent[num] = num
        
        def find(node):
            if parent[node] == node:
                return node
            parent[node] = find(parent[node])
            
            return parent[node]
        
        def union(u, v):
            p1, p2 = find(u), find(v)
            
            if p1 != p2:
                parent[u] = parent[v]
                
        setNums = set(nums)
        # print(sorted(list(setNums)))
        for num in nums:
            if num + 1 in setNums:
                union(num, num + 1)
                
        for num in setNums:
            count[find(num)] += 1

        
        return max(count.values())
            
                
        
        