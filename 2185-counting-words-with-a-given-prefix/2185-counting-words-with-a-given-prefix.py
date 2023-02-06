class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        first_count = len(pref)
        count = 0
        
        for word in words:
            if word[:first_count] == pref:
                count += 1
                
        return count
            
        