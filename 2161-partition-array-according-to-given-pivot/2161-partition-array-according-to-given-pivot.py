class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lessthan = []
        greaterthan = []
        equal = []
        result = []
        for i in range(len(nums)):
            if nums[i] < pivot:
                lessthan.append(nums[i])
            elif nums[i] > pivot:
                greaterthan.append(nums[i])
            else:
                equal.append(nums[i])
                
        # lessthan.sort()
        result += (lessthan + equal + greaterthan)
        
        return result
        