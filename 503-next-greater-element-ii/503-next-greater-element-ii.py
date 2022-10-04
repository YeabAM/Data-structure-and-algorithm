class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        monotone = []
        ans = [-1 for _ in range(len(nums))]
        for i in range(len(nums)):
            # print("d", monotone)
            while monotone and nums[monotone[-1]] < nums[i]:
                idx = monotone.pop()
                ans[idx] = nums[i]
                
            monotone.append(i)
            
        index = 0 
        # print(monotone)
        while len(monotone) > 1:
            curr = monotone.pop()
            # print("curr", curr)
            for i in range(index, curr):
                if nums[i] > nums[curr]:
                    # print("check", i)
                    index = i
                    ans[curr] = nums[i]
                    break
                    
        return ans
                
            
            
        