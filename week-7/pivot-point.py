class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        psumlist = []
        psum = 0
        for i in range(len(nums)-1,-1,-1):
            psum += nums[i]
            psumlist.append(psum)
        print(psumlist)
        psum = 0
        for i in range(len(nums)):
            psum += nums[i]
            if psum == psumlist.pop():
                return i
        
        return -1
                
            
        