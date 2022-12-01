class Solution:
    
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    # if the substring of size 2 and below or if the inner substsring is already a palindrome
                    if j - i <= 1 or dp[i+1][j-1]:
                        dp[i][j] = 1
                        
        main_dp = [-1 for _ in range(n+1)]
        
        for i in range(n-1, -1, -1):
            
            minCut = float('inf')
            
            for j in range(i, n):
                
                if dp[i][j]:
                    minCut = min(minCut, main_dp[j+1] + 1)
                    
            main_dp[i] = minCut
            
        
        return main_dp[0]
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    

        
        
        
        
        
    
        