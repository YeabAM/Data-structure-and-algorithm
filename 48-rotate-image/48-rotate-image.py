class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        up = 0
        down = len(matrix) - 1
        
        while up < down:
            for i in range(len(matrix[0])):
                matrix[up][i], matrix[down][i] = matrix[down][i], matrix[up][i]
            up += 1
            down -= 1

        for i in range(len(matrix)):
            for j in range(i, len(matrix[i])):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]