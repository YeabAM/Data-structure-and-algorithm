class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        count1 = Counter(word1)
        count2 = Counter(word2)
        
        word1 = set(word1)
        word2 = set(word2)
        
        uniq1 = len(count1)
        uniq2 = len(count2)
        
        
        for c1 in word1:
            for c2 in word2:
                
                count1[c1] -= 1
                count2[c1] += 1
                count1[c2] += 1
                count2[c2] -= 1
                
                if count2[c2] == 0:
                    del count2[c2]
                
                if count1[c1] == 0:
                    del count1[c1]
                    
                if len(count1) == len(count2):
                    return True
                
                count1[c1] += 1
                count2[c1] -= 1
                count1[c2] -= 1
                count2[c2] += 1
                
                if count2[c1] == 0:
                    del count2[c1]
                
                if count1[c2] == 0:
                    del count1[c2]
                    
        return False
                
                
                
                
    
    
    

