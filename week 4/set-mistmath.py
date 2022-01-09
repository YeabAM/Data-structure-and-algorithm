class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        temp = list(range(1,len(nums)+1))
        temp2 = []
        count = Counter(nums)
        nums.sort()
        for i in range(len(nums)):
            if count[temp[i]] == 2:
                temp2.insert(0,nums[i])
            elif count[temp[i]] == 0:
                 temp2.append(temp[i])
        return temp2