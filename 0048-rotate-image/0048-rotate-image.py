class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        rows = len(matrix)
        cols = len(matrix[0])
    
        for r in range(rows):
            for c in range(r+1, cols):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
            
        for i in range(rows):
            matrix[i] = matrix[i][::-1]
            
        
        