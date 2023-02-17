class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        
        for i, l in enumerate(s):
            if counter[l] == 1:
                return i
            
        return -1
        