class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        memo = {}
        def dp(idx):
            if idx in memo:
                return memo[idx]
            if idx + nums[idx] >= len(nums) - 1 or idx == len(nums) - 1:
                return 1
            _min = float('inf')
            for i in range(1, nums[idx]+1):
                if i + idx < len(nums) - 1:
                    _min = min(_min, dp(i + idx) + 1)
            memo[idx] = _min
            return _min
        return dp(0)