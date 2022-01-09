class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapper = {}
        isIsomorphic = True
        for i in range(len(s)):
            if s[i] in mapper.keys() and t[i] in mapper.values():
                if mapper[s[i]] == t[i]:
                    continue
                else:
                    isIsomorphic = False
                    break                    
            elif s[i] not in mapper.keys() and t[i] not in mapper.values():
                mapper[s[i]] = t[i]                
            else:
                isIsomorphic = False
                break
                                  
        return isIsomorphic