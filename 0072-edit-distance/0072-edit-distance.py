class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[1 for _ in range(len(word1) + 1)] for _ in range (len(word2) + 1)]
        
        
        for j in range(len(dp[0])):
            dp[0][j] = j
            
        for  i in range(len(dp)):
            dp[i][0] = i
                
        
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                insert = delete = replace = 0
                    
                if word2[i-1] == word1[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                
            
                else:
                    insert = dp[i - 1][j]
                    delete = dp[i][j - 1]
                    replace = dp[i-1][j-1]
                    
                    dp[i][j] += min(insert, delete, replace)
                    
        
        return dp[len(word2)][len(word1)]
                    
                
        
        
        