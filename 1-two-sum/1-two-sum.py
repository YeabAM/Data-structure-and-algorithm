class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        count = defaultdict(list)
        
        for i,n in enumerate(nums):       
            count[n].append(i)  
        
        for i,n in enumerate(nums):
            if (target - n) in count: 
                if (2*n) == target:
                    if len(count[n]) == 2:
                        return count[n]
                    else:
                        continue
                else:
                    return [i, count[target-n][0]]
                
            
                
                
        
        
                
            
            
            
        