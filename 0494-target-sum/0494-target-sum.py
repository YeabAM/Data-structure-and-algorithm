class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        @lru_cache(None)
        def count_ways(idx, pos, total):
            if idx >= len(nums):
                return 1 if total == target else 0
            
            if pos:
                total += nums[idx]
            else:
                total -= nums[idx]
            
            if idx == len(nums) - 1 :
                option_1 = count_ways(idx+1, not pos, total)
                option_2 = 0
                
            else:
                option_1 = count_ways(idx+1, not pos, total)
                option_2 = count_ways(idx+1, pos, total)
            
            # print(idx, pos, option_1, option_2)
            
            return option_1 + option_2
        
        
        option_1 = count_ways(0, True, 0)
        option_2 = count_ways(0, False, 0)
        
        # print(option_2)
        
        return option_2 +option_1
        