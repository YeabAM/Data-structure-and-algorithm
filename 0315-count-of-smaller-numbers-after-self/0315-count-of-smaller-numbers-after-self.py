class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sort_list, res = [], []
        
        for i in range(len(nums) - 1, -1, -1):
            count = bisect.bisect_left(sort_list, nums[i])
            res.append(count)
            sort_list.insert(count, nums[i])
            
        return res[::-1]
        