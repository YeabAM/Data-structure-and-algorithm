class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def customi(val):
            summ = 0 
            for i in nums:
                summ += ceil(i/val)
            return summ
        
        maximus = max(nums)
     
        
        # for i in range(1, maximus + 1):
        left = 1
        right = maximus
        big = float("inf")    
    
        while left <= right:
            mid = left + ( right - left) // 2
            
            check = customi(mid)
            # print(check, mid)
            if check <= threshold:                    
                right = mid - 1
                big = min(big,mid)
                    
            elif check > threshold:

                left = mid + 1
            
        return big

                 
          
           
        
        