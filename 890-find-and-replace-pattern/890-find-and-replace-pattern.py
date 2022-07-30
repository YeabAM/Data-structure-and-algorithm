class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        result = []
        
        for word in words:
        
            # print("w->", word)
            mutation = dict()
            
            match = True
            for i in range(len(word)):
                if word[i] not in mutation:
                    if pattern[i] not in mutation.values():
                        mutation[word[i]]=pattern[i]
                    else:
                        match = False
                        
                else:
                    if mutation[word[i]] != pattern[i]:
                        match = False
                    
            if match:
                result.append(word)
                    
                
                

            

        return result
                        
                
        
        
        