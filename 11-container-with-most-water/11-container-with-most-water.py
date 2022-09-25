class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxWater = float('-inf')
        
        while left < right:
            h = min(height[left], height[right])
            w = right - left 
            maxWater = max(maxWater, h * w)
            
            if height[left] > height[right]:
                right -= 1
                
            elif height[left] < height[right]:
                left += 1
            
            else:
                right -= 1
                left += 1
                
        return maxWater
                
            
        