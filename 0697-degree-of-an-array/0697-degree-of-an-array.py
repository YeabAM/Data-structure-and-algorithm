class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        mainCounts = Counter(nums)
        degree = max(mainCounts.values())
        running = defaultdict(int)
        l = 0
        minLen = float('inf')
        
        for r in range(len(nums)):
            
            running[nums[r]] += 1
            deg = max(running.values())
            
            while deg >= degree and l <= r:
                curr = r - l + 1    
                minLen = min(minLen, curr)
                left = nums[l]
                running[left] -= 1
                deg = max(running.values())
                l += 1
                
        return minLen
                
                
            
        