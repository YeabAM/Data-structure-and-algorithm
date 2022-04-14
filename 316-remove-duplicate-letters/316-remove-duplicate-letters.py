class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        removed = []
        count = Counter(s)
        visited = set()
        
        for i in range(len(s)):
            if s[i] in visited:
                count[s[i]] -= 1
                continue
            if not removed:
                removed.append(s[i])
                visited.add(s[i])
                count[s[i]] -= 1
            
            elif s[i] < removed[-1]:
                while removed:   
                    if s[i] < removed[-1] and  count[removed[-1]] > 0:
                        visited.discard(removed[-1])
                        removed.pop()
                        
                    else:
                        break
                removed.append(s[i])
                visited.add(s[i])
                count[s[i]] -= 1
            elif s[i] > removed[-1]:
                removed.append(s[i])
                visited.add(s[i])
                count[s[i]] -= 1
            else:
                count[s[i]] -= 1
            
            
        return "".join(removed)   
                
                
            
        