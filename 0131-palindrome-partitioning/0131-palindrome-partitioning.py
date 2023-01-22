class Solution:
    def isPalindrome(self, s, l, r):
        
        while l < r:
            if s[l] != s[r]:
                return False
            
            l += 1
            r -= 1
            
        return True
    
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def dfs(idx, part):
            if idx >= len(s):
                res.append(part)
                return
            
            for i in range(idx, len(s)):
                if self.isPalindrome(s, idx, i):
                    curr = s[idx:i+1]
                    dfs(i+1, part + [curr])
                    
        dfs(0,[])
        
        return res