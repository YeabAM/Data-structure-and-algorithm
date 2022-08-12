class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        def dp(path):
            curr = "".join(path)
            
            if curr == s:
                return True
            
            if curr != s[:len(curr)]:
                return False
            
            for word in wordDict:
                if dp(path + [word]):
                    res.append(path + [word])
                    
                    
        dp([])
        
        return [ " ".join(res[i]) for i in range(len(res))]
                
        