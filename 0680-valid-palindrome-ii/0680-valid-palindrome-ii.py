class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def dfs(l, r, count):
            if count > 1:
                return False
            
            if l >= r:
                return True
            
            if s[l] == s[r]:
                return dfs(l+1, r-1, count)
            
            else:
                return (dfs(l,r-1, count + 1) or dfs(l+1, r, count + 1))
            
        return dfs(0, len(s) - 1, 0)