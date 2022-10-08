class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        
        MaxArea = float('-inf')
        
        
        while left < right:
            h = min(height[left], height[right])
            w = right - left
            currArea =  h * w
            
            MaxArea = max(MaxArea, currArea)
            
            if height[left] <= height[right]:
                left += 1
                
            else:
                right -= 1
                
        return MaxArea
                
            
            
            
        
        
        
        
        