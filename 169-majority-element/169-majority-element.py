class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        current = 0
        count = 1
        nums.sort()
        
        
        if len(nums)  <= 2:
            return nums[0]
        
        for i in range(1, len(nums)):
#             
            
            if nums[current] != nums[i]:
               
                if count > len(nums) // 2:
                    # print("got it",nums[current], count)
                    break
                else:
                    # print("nope",nums[current],nums[i])
                    count = 1
                    current = i
                    # print("n", current, count)
                    
            else:
                # print(nums[current],nums[i])
                count += 1
                
        return nums[current]
                    
        