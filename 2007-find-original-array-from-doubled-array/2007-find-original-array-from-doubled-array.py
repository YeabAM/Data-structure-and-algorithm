class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2:
            return []
        changed.sort()
        counts = Counter(changed)
        half = len(changed) // 2
        res = []
        
        for num in changed:
            if num == 0 and counts[num] % 2 == 0 and counts[0] != 0:
                counts[0] -= 2
                if counts[0] == 0:
                    del counts[0] 
                res.append(0)
                
            else:  
                if num in counts and (num*2) in counts and num != 0:    
                    counts[num] -= 1
                    counts[num*2] -= 1
                    if counts[num] == 0:
                        del counts[num]
                    if counts[num*2] == 0:
                        del counts[num*2]

                    res.append(num)
                
                
        if len(changed) // 2 == len(res):
            return res
        else:
            return []
        
        
        
                
        