class Solution:
    def trap(self, height: List[int]) -> int:
        size = len(height)
        leftMax = [0 for _ in range(size)]
        rightMax = [0 for _ in range(size)]
        
        currMax = 0
        
        for i in range(size):
            leftMax[i] = currMax
            currMax = max(height[i], currMax)
                
        currMax = 0
                
        for i in range(size -1 , -1, -1):
            rightMax[i] = currMax
            currMax = max(height[i], currMax)
                
        totalWater = 0
                
        for i in range(size):
            h = min(leftMax[i], rightMax[i])
            curr = height[i]
            
            if curr < h:
                totalWater += h - curr           
        return totalWater
        
        