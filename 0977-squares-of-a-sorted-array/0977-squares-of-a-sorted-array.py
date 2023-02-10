class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1
        square_arr = []
        
        while l <= r:
            squ_l = nums[l] ** 2
            squ_r = nums[r] ** 2
            
            if squ_l < squ_r:
                square_arr.append(squ_r)
                r -= 1
                
            else:
                square_arr.append(squ_l)
                l += 1
                
        return square_arr[::-1]
        