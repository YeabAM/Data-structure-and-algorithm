class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board),len(board[0]) 
        
        def helper(visited, i, j, count):
            if i > rows-1 or j > cols-1 or i < 0 or j <0:
                return False 
            
            if count > len(word)-1:
                return False
             
            if board[i][j] != word[count]:
                return False
            
            if visited[i][j]:
                return False 

            if count == len(word)-1:
                return True 

            visited[i][j] = True
            
            count+=1 
            d = helper(visited, i+1, j, count) 
            u = helper(visited, i-1, j, count)
            r = helper(visited, i, j+1, count) 
            l = helper(visited, i, j-1, count) 
            visited[i][j] = False
            return d or u or r or l

        visited = [[False for x in range(cols)] for y in range(rows)]
        for i in range(rows):
            for j in range(cols): 
                if helper(visited,i,j, 0):
                    return True

        return False   