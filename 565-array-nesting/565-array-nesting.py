class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        maxx = 0
        visited = set()
        count  = 0
        def dfs(index):
            nonlocal count
            visited.add(index)
            count += 1
            
            if nums[index] not in  visited:
                dfs(nums[index])
                
        for num in nums:
            if num not in visited:
                dfs(num)
                maxx = max(count, maxx)
                count = 0
                
        return maxx
            
            
            
        