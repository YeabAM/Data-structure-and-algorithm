class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        missing = -1
        duplicate = -1
        
        for n in nums:
            count[n] += 1
            
        for num in range(len(nums)):
            if num+1 not in count:
                missing = num+1
            elif count[num+1] == 2:
                duplicate = num+1
                
        return [duplicate, missing]
                
            
            
            
            
            
        