class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0    
        
        for Type, Color, Name in items:
            if ruleKey == "type" and Type == ruleValue:
                count += 1
            elif ruleKey == "color" and Color == ruleValue:
                count += 1
            elif ruleKey == "name" and Name == ruleValue:
                count += 1
                
        return count
        