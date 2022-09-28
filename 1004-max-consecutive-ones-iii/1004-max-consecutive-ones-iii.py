class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        answer = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                k -= 1
            while k < 0 and l <= r:
                if nums[l] == 0:
                    k += 1
                l += 1
            answer = max(answer, r-l+1)

        return answer