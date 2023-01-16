class Solution:
    def longestArithSeqLength(self, arr: List[int]) -> int:
        max_dif = max(arr) - min(arr)
        max_len = 0
        
        def count(difference):
            dp = defaultdict(int)
        
            for i in range(len(arr)):
                dp[arr[i]] = 1 + dp[arr[i] - difference]

            max_length = 0
            # print(dp)

            for val in dp.values():
                max_length = max(val, max_length)

            return max_length
        
        
        for i in range(max_dif + 1):
            pos = count(i)
            neg = count(-1 * i)
    
            max_len = max(pos, neg, max_len)
            
            
        return max_len
        
        
        
        
        
            