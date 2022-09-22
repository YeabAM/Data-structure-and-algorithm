class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        letters = list(s)
        
        for i in range(0,len(s),2*k):
            letters[i:i+k] = reversed(letters[i:i+k])
            
        return "".join(letters)
            
            
        