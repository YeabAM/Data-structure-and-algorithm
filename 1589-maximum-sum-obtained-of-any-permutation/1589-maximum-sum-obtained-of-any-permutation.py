class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        
        freq = [0 for _ in range(len(nums))]
        
        for l, r in requests:
            freq[l] += 1
            if r+1 < len(nums):
                freq[r + 1] -= 1
                
        for i in range(1, len(freq)):
            freq[i] += freq[i-1]
            
        freq.sort()
        nums.sort()
        total = 0
        
        for i in range(len(nums)-1, -1, -1):
            total += freq[i] * nums[i]
            
        return total % 1000000007
            
            
        