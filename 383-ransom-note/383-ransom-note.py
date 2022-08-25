class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        rn_count = Counter(ransomNote)
        ma_count = Counter(magazine)
        
        for i in rn_count:
            if ma_count[i] < rn_count[i]:
                return False
        
        return True