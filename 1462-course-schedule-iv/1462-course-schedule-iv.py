class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        dp = [[0 for _ in range(numCourses)] for _ in range(numCourses)]
        
        
        for preq, cour in prerequisites:
            dp[preq][cour] = True
            
        
        for k in range(numCourses):
            
            for i in range(numCourses):
                
                for j in range(numCourses):
                    
                    directConnect = dp[i][j]
                    dp[i][j] = directConnect or (dp[i][k] and dp[k][j])
        ans = []          
        for f, t in queries:
            ans.append(dp[f][t])
            
        return ans
        
                    
        
                    
                    
                    
                    
                            
            
        