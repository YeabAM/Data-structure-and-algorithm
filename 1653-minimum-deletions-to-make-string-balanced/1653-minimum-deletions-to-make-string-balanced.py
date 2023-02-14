class Solution:
    def minimumDeletions(self, s: str) -> int:
        min_opt = min(s.count('a'), s.count('b'))
        
        forward_count = [0 for _ in range(len(s) + 1)]
        backward_count = [0 for _ in range(len(s) + 1)]
        
        
        for i in range(1, len(s) + 1):
            if s[i-1] == 'b':
                forward_count[i] = forward_count[i-1] + 1
                
            else:
                forward_count[i] = forward_count[i-1]
                
        for j in range(len(s) - 1, -1, -1):
            if s[j] == 'b':
                backward_count[j] = backward_count[j+1] + 1
                
            else:
                backward_count[j] = backward_count[j+1]
        

        
        for i in range(len(s)):
            to_a = forward_count[i+1]
            to_b = (len(s) - i -1) - (backward_count[i])
            
            total = to_a + to_b
            
            min_opt = min(total, min_opt)
            
        
        return min_opt
                
        