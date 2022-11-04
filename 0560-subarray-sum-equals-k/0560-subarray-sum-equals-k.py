class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        psum = 0
        count = 0
        psumdict = defaultdict(int)
        
        for i in range(len(nums)):
            psum += nums[i]
            
            if psum == k:
                count += 1
            if (psum - k) in psumdict:
                count += psumdict[psum - k]
            
            psumdict[psum] += 1
            
        return count