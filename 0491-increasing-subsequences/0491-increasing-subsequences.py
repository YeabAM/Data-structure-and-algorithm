class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        
        def backt(path, idx):
            if idx >= len(nums):
                if len(path) > 1:
                    ans.add(tuple(path))
                return
            
            if not path or  path[-1] <= nums[idx]:
                backt(path + [nums[idx]], idx + 1)
            backt(path, idx + 1)
                    
        backt([], 0)
        return list(ans)
            
                
        