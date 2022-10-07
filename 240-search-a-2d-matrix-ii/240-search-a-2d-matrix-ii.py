class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        c, r = len(matrix[0]) - 1, 0
        
        while r < len(matrix) and c >= 0:
            # print(r, c)
            if matrix[r][c] == target:
                return True
            
            elif matrix[r][c] > target:
                c -= 1
                
            
            else:
                r += 1
        
        while r < len(matrix):
            if matrix[r][0] == target:
                return True
            r += 1
            
        while c >= 0:
            if matrix[len(matrix)-1][c] == target:
                return True
            c -= 1
            
        return False
                
        