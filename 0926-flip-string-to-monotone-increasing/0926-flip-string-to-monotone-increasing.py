class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        min_opt = min(s.count('1'), s.count('0'))
        
        forward_count = [0 for _ in range(len(s) + 1)]
        backward_count = [0 for _ in range(len(s) + 1)]
        
        
        for i in range(1, len(s) + 1):
            if s[i-1] == '1':
                forward_count[i] = forward_count[i-1] + 1
                
            else:
                forward_count[i] = forward_count[i-1]
                
        for j in range(len(s) - 1, -1, -1):
            if s[j] == '1':
                backward_count[j] = backward_count[j+1] + 1
                
            else:
                backward_count[j] = backward_count[j+1]
        

        
        for i in range(len(s)):
            to_zero = forward_count[i+1]
            to_one = (len(s) - i -1) - (backward_count[i])
            # print(to_zero, to_one)
            total = to_zero + to_one
            
            min_opt = min(total, min_opt)
            
        
        return min_opt
                
            
                
                