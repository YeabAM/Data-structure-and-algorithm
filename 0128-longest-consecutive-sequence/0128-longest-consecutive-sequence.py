class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        arr = nums
        arr.sort()
        nonDuplicate = [arr[0]]
        for i in range(len(arr)):
            if nonDuplicate[-1] != arr[i]:
                nonDuplicate.append(arr[i])
        left = right = 0
        res = 1
        while right < len(nonDuplicate):
            while right+1 < len(nonDuplicate) and nonDuplicate[right] == nonDuplicate[right+1]-1:
                right += 1
            res = max(res, right-left+1)
            right += 1
            left = right
        return res