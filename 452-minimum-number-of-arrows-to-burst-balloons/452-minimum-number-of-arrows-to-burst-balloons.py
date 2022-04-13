class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        curr = [points[0][1]]
        # print(curr)
        for i in range(len(points)):
            if points[i][0] <= curr[-1] and curr[-1] <= points[i][1]:
                continue
            curr.append(points[i][1])
        
        return len(curr)
            
         