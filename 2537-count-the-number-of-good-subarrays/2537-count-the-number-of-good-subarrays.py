class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        counter = defaultdict(int)
        # counter = Counter()
        left = 0
        pairs = 0
        count = 0
        
        for r in range(len(nums)):
            counter[nums[r]] += 1
            pairs += counter[nums[r]] - 1
            
            while pairs >= k and left < r:
                # print(left, r,pairs)
                count += len(nums) - r 
                counter[nums[left]] -= 1
                pairs -= counter[nums[left]]
                left += 1
                # print(pairs)
                
        return count
                
            
            
        