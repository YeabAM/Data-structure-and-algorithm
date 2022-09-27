class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        pos = {}
        
        for  idx, num in enumerate(nums):
            if num in pos:
                if abs(pos[num] - idx) <= k:
                    return True
            pos[num] = idx
                
        return False
                
            