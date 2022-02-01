class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        total = 0
        _max = 0
        for val in nums:
            if val < _max:
                diff = _max - val
                _max = val + diff + 1
                total += diff
            else:
                _max = val + 1
        return total     