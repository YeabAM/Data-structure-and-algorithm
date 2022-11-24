class Solution:
    def trap(self, height: List[int]) -> int:
        size = len(height)
        leftMax = [0 for _ in range(size)]
        rightMax = [0 for _ in range(size)]
        
        currMax = 0
        
        for i in range(size):
            if height[i] >= currMax:
                leftMax[i] = height[i]
                currMax = height[i]
            else:
                leftMax[i] = currMax
                
        currMax = 0
                
        for i in range(size -1 , -1, -1):
            if height[i] >= currMax:
                rightMax[i] = height[i]
                currMax = height[i]
            else:
                rightMax[i] = currMax
                
        totalWater = 0
        
        
        
        for i in range(size):
            
            w = min(leftMax[i], rightMax[i])
            h = height[i]
            
            totalWater += abs(w - h)
            # print(i, leftMax[i], rightMax[i], totalWater)
            
        return totalWater
        
        