class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = Counter(nums)
        half = len(nums) // 2
        
        for num in counts:
            if counts[num] > half:
                return num
        