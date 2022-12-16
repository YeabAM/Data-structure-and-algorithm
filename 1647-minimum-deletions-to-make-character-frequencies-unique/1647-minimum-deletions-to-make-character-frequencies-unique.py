class Solution:
    def minDeletions(self, s: str) -> int:
        count = [0 for i in range(26)]
        operation = 0
        for ch in s:
            count[ord(ch) - 97] += 1
            
        count.sort()
        
        for i in range(24, -1, -1):
            if count[i] == 0:
                break
                
            if count[i] >= count[i+1]:
                op = min(count[i] - count[i+1] + 1, count[i])
                count[i] -= op
                operation += op
        
        return operation