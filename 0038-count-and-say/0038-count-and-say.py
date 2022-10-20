class Solution:
    def count(self, num):
        cnt = []
        i = 0
        
        while i < len(num):
            j = i + 1
            
            while j < len(num) and num[i] == num[j]:
                j += 1
                
            
            cnt.append(str(j - i))
            cnt.append(num[i])
            i = j
            
        return(''.join(cnt))
            
        
    def countAndSay(self, n: int) -> str:
        curr = '1'
        
        for _ in range(n - 1):
            curr = self.count(curr)
            
        return curr
    

        
        
        
        