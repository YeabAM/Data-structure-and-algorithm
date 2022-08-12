class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # days.sort()
        
        def dp(arrival):
            if arrival in memo:
                return memo[arrival]
            if arrival >= len(days):
                return 0
            
            
            memo[arrival] =  min(dp(bisect.bisect_left(days, days[arrival] + 1)) + costs[0],
            dp(bisect.bisect_left(days, days[arrival] + 7)) + costs[1],
            dp(bisect.bisect_left(days, days[arrival] + 30)) + costs[2])
            
            return memo[arrival]
        
        
        memo = {}
        return dp(0)
            
            
        