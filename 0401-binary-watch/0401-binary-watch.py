class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = []
        
        def reading(index, H, M, setCount):
            
            if setCount == 0:
                if M < 10:
                    M = f'0{M}'
                read = f'{H}:{M}'
                
                ans.append(read)
                
                return
                
            if index >= 10:
                return
                 
            if index < 4:
                currH = H + 2 ** index
                if currH < 12:
                    reading(index+1, currH, M, setCount - 1)
                    
                reading(index+1, H,M,setCount)
                
            else:
                
                currM = M + 2 ** (index - 4)
                if currM < 60:
                    reading(index+1, H, currM, setCount - 1)
                
                reading(index+1,H,M,setCount)
                
        reading(0,0,0,turnedOn)
        
        return ans
                
                    
                    
                