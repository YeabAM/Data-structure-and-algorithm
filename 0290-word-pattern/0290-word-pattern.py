class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = list(s.split())
            
        if len(pattern) != len(s):
            
            return False
        
        match = defaultdict(lambda : None)
        visited = set()
        
        for idx in range(len(pattern)):
            
            if pattern[idx] not in match and s[idx] not in visited:
                match[pattern[idx]] = s[idx]
                visited.add(s[idx])
                
            else:
                if pattern[idx] not in match:
                    return False
                elif match[pattern[idx]] != s[idx]:
                    return False
                              
                
        return True
                
        