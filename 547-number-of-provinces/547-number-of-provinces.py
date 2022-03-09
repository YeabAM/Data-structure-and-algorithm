class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        n = len(isConnected)
        
        def dfs(row):
            for col in range(n):
                if isConnected[row][col] == 1 and col not in visited:
                    visited.add(col)
                    dfs(col)
           
        count = 0
        for i in range(n):
            if i not in visited:
                count += 1
                visited.add(i)
                dfs(i)
        return count
            
                
        
        
        
        