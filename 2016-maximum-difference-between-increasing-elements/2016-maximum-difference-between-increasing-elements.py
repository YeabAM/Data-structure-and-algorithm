class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        curr_min = nums[0]
        max_dif = float('-inf')
        
        for num in nums[1:]:
            if num > curr_min:
                # print(num, curr_min)
                max_dif = max(max_dif, num - curr_min)
            else:
                curr_min = num
        
        return max_dif if max_dif != float('-inf') else -1