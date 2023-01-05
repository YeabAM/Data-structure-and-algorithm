class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        
        arrow = points[0][1]
        
        count = 1
        
        for i in range(1, len(points)):
            if points[i][0] > arrow:
                count += 1
                arrow = points[i][1]
                
        return count
                
            
        