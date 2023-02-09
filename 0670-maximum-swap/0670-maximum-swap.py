class Solution:
    def maximumSwap(self, num: int) -> int:
        numstr = list(str(num))
        sorted_num = sorted(numstr, reverse = True)
        
        
        for i in range(len(numstr)):
            if numstr[i] != sorted_num[i]:
                val = sorted_num[i]
    
                pos = -1
                for j in range(len(numstr)):
                    if numstr[j] == val:
                        pos = j
                        
                numstr[i], numstr[pos] = numstr[pos], numstr[i]
                break
                
                    
                    
        return int("".join(numstr))
    
        
        
        
        
        
        