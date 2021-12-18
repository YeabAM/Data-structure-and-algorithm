class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr=[]
        count=0
        for i in nums:
            count=0
            current=i
            for j in nums:
                if current>j:
                    count+=1
            arr.append(count)   
        return arr