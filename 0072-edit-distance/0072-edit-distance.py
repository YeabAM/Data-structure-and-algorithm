class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        def edit(w1, w2):
            if (w1, w2) in memo:
                return memo[(w1, w2)]
            
            if w1 == len(word1) and w2 == len(word2):
                memo[(w1, w2)] = 0
                return 0
            
            if w1 == len(word1):
                memo[(w1, w2)] = len(word2) - w2
                return memo[(w1, w2)]
            
            if w2 == len(word2):
                memo[(w1, w2)] = len(word1) - w1
                return memo[(w1, w2)]
            
            if word1[w1] == word2[w2]:
                memo[(w1, w2)] = edit(w1 + 1, w2 + 1)
                return memo[(w1, w2)]
            
            insert = delete = replace = 0
            if word1[w1] != word2[w2]:
                insert = edit(w1, w2 + 1)
                delete = edit(w1 + 1, w2 + 1)
                replace = edit(w1+1, w2)
                
                memo[(w1, w2)] = 1 + min(insert, delete, replace)
                return memo[(w1, w2)]
            
            
        memo = {}
        minOps = edit(0,0)
        
        return minOps
                
                
        
        
        