class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        answer = copy.deepcopy(mat)
        
        in_bound = lambda r, c: 0 <= r < len(mat) and 0 <= c < len(mat[0])
        
        prefix_sum = [[0 for _ in range(len(mat[0]) + 1)] for _ in range(len(mat) + 1)]
        
        
        for r in range(1, len(mat) + 1):
            for c in range(1, len(mat[0]) + 1):
                prefix_sum[r][c] = mat[r-1][c-1] + prefix_sum[r-1][c] + prefix_sum[r][c-1] - prefix_sum[r-1][c-1]
                
        
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                right_bottom = (min(len(mat) - 1, r + k), min(len(mat[0])-1, c + k))
                top_left = ((max(0, r - k)), max(0, c - k))
                
                value = prefix_sum[right_bottom[0] + 1][right_bottom[1] + 1]
            
                value -= prefix_sum[top_left[0]][right_bottom[1] + 1]
                value -= prefix_sum[right_bottom[0] + 1][top_left[1]]

                
                value += prefix_sum[top_left[0]][top_left[1]]
                answer[r][c] = value
                
        return answer
                
                