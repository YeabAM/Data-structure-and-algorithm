class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(int)
        
        for i in range(len(arr)):
            dp[arr[i]] = 1 + dp[arr[i] - difference]
            
        max_length = 0
        # print(dp)
        
        for val in dp.values():
            max_length = max(val, max_length)
            
        return max_length
        
        
        
        
        
        