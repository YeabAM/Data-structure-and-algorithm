class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def dp(isPlayer1, total1, total2, i, j):
            
            if i > j:
                return total1 >= total2
                
            if isPlayer1:
                return dp(not isPlayer1, total1, total2 + nums[j], i , j-1) and dp(not isPlayer1, total1, total2 + nums[i], i+ 1 , j)
            
            else:
                return dp(not isPlayer1, total1 + nums[j], total2, i , j-1) or dp(not isPlayer1, total1 + nums[i], total2, i+ 1 , j)
            
        return dp(False, 0, 0, 0, len(nums)-1)
            
                
        