class Solution:
    def robotWithString(self, s: str) -> str:
        count = [0 for _ in range(26)]
        
        for ch in s:
            pos = ord(ch) - 97
            count[pos] += 1
            
            
        def check(pos):
            for i in range(pos):
                if count[i] > 0:
                    return True
            
            return False
                    
            
        final_word = []
        stack = []
        
        for ch in s:
            pos = ord(ch) - 97
            count[pos] -= 1
            stack.append(ch)
            
            while stack:
                curr = stack[-1]
                pos = ord(curr) - 97
                
                if not check(pos):
                    final_word.append(stack.pop())
                
                else:
                    break
            
            
        return "".join(final_word)                
                    
          
                
            
            
        