class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr = nums
        numset = set(arr)
        result = 0
        for i in range(len(arr)):
            if arr[i]-1 not in numset:
                cur = arr[i]
                count = 0
                while cur in numset:
                    cur += 1
                    count += 1
                result = max(result, count)
        return result