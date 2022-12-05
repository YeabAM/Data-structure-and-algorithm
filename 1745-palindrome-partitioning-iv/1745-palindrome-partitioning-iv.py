class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        palDp = [[0 for _ in range(n)] for _ in range(n)]
        
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if s[i] == s[j]:
                    if j - i <= 1 or palDp[i+1][j-1]:
                        palDp[i][j] = 1
                        
        # print(palDp)
        
        for i in range(n - 2):
            if palDp[0][i]:
                for j in range(i+1, n-1):
                    if palDp[i+1][j] and palDp[j+1][n-1]:
                        return True
        
        return False
                    
        
        