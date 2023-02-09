class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        l = 0
        goodsubs1 = 0
        
        for r in range(len(nums)):
            counts[nums[r]] += 1
            
            while len(counts) > k and l <= r:
                counts[nums[l]] -= 1
                
                if counts[nums[l]] == 0:
                    del counts[nums[l]]
            
                l += 1
            
            goodsubs1 += r - l + 1
               
        k -= 1
        goodsubs2 = 0
        counts = defaultdict(int)
        l = 0
        
        for r in range(len(nums)):
            counts[nums[r]] += 1
            
            while len(counts) > k and l <= r:
                counts[nums[l]] -= 1
                
                if counts[nums[l]] == 0:
                    del counts[nums[l]]
            
                l += 1
            
            goodsubs2 += r - l + 1
            
        # print(goodsubs1, goodsubs2, k)
        return goodsubs1 - goodsubs2