class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        p1 = 0
        p2 = n
        res = []
        
        while p2 < 2*n:
            res.append(nums[p1])
            res.append(nums[p2]) 
            p1 += 1
            p2 += 1
            
        return res
            