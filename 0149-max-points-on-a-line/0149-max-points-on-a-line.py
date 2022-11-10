class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
        maxPoints = 2
        
        for i in range(len(points) - 1):
            x, y = points[i]
            slopeCount = {}
            # print('-------------')
            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                
                #vertical line
                if abs(x2 - x) == 0:
                    slopeCount[float('inf')] = 1 + slopeCount.get(float('inf'), 0)
                    continue
                    
                currSlope = (y2 - y) / (x2 - x)
                
                # print('m', x, y, x2, y2, currSlope)
                
                slopeCount[currSlope] = 1 + slopeCount.get(currSlope, 0)
            # print(x, y, slopeCount)
            currMax = 1 + max(slopeCount.values())  
            maxPoints = max(currMax, maxPoints)
            
        return maxPoints
                
        