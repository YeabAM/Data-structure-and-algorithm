class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        minOps = float('inf')
        currCount = 0
        
        
        for right in range(len(blocks)):
            if blocks[right] == 'W':
                currCount += 1
                
            k -= 1
            
            if k == 0:
                minOps = min(minOps, currCount)
                
                if blocks[left] == 'W':
                    currCount -= 1
                    
                k += 1
                left += 1
                
        return minOps