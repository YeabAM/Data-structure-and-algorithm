class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr = []
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            if abs(nums[start]) > abs(nums[end]):
                arr.append(nums[start] * nums[start])
                start += 1
            else:
                arr.append(nums[end] * nums[end])
                end -= 1
        arr = arr[::-1]
        return arr
                