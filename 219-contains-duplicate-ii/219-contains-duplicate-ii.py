class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        occur = defaultdict(list)
        
        for i, n in enumerate(nums):
            occur[n].append(i)
            
        for oc in occur:
            for j in range(len(occur[oc]) - 1):
                if occur[oc][j+ 1] - occur[oc][j] <= k:
                    return True
        return False
                
                
                
                
                
        
        