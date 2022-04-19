class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        inc = [0] * (len(security) + 1)
        dec = [0] * (len(security) + 1)
        ans = []
        for i in range(len(security) - 1):
            if security[i] >= security[i+1]:
                dec[i + 1] = 1 + dec[i]
                
        
        
        for i in range(len(security) - 1, 0, -1):
            if security[i] >= security[i-1]:
                inc[i - 1] = 1 + inc[i]
                
        for i in range(len(security)):
            if inc[i] >= time and dec[i] >= time:
                ans.append(i)
        
        return ans
                
                
        
            
                
            
        