class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums.sort(key= lambda x: int(x), reverse=True)
        kSmallest = nums[k-1]
        return kSmallest