class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l = max(nums)
        h = sum(nums)
        
        while l < h:
            mid = (h + l) // 2
            total = 0
            count = 1
            
            for n in nums:
                
                if total + n <= mid:
                    total += n
                
                else:
                    total = n
                    count += 1
                    
                    
            if count > k:
                l = mid + 1
                
            else:
                h = mid
                
        return h
                    
                
                    
                
                
                
        