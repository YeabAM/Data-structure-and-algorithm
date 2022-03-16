class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid)):
            left = 0
            right = len(grid[0]) - 1
            first = -1
            while left <= right:
                mid = (left + right) // 2
                if grid[i][mid] >= 0:
                    left = mid + 1
                if grid[i][mid] < 0:
                    right = mid - 1
                    first = mid
            
            if first != -1:
                count += ((len(grid[i]) - 1) - first) + 1
            
        return count
             
                 
                 
                
            
        