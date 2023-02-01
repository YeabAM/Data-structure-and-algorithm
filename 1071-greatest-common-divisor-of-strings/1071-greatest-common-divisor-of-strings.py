class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        possibles = []
        cur = []
        
        def checkPrefix(word):
            k = len(word)
            for i in range(0, len(str1), len(word)):
                curr = str1[i: i+k]
                if curr != word:
                    return False
                
            for j in range(0, len(str2), len(word)):
                curr = str2[j:j+k]
                if curr != word:
                    return False
                
            return True
            
            
    
        length = min(len(str1), len(str2))
        
        for i in range(length):
            if str1[i] == str2[i]:
                cur.append(str1[i])
                possibles.append("".join(cur))
                       
        
        for word in reversed(possibles):
            if checkPrefix(word):
                return word
            
        return ""