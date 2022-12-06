class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        dp = [1] * len(arr)
        
        last = "I"
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1] and last == "I":
                dp[i] += dp[i - 1]
                last = "D"
            elif arr[i] > arr[i - 1] and last == "D":
                dp[i] += dp[i - 1]
                last = "I"
            else:
                if arr[i] != arr[i-1]:
                    last = "I" if arr[i] > arr[i - 1] else"D"
                    dp[i] += 1
                    
        maxx = max(dp)
        return maxx
        
                