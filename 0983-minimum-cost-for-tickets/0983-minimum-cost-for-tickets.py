class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        days.sort()
        
        @lru_cache(None)
        def travel(idx):
            if idx >= len(days) or idx < 0:
                # print('here')
                return 0
            
            #one day
            temp = days[idx] + 1
            next_one_day = bisect.bisect_left(days, temp)
            temp2 = bisect.bisect_right(days, temp)
            # print(temp2, next_one_day, temp,'h')
            one_day = travel(next_one_day)
            
            #7 day
            temp = days[idx] + 7
            next_seven_day = bisect.bisect_left(days, temp)
            seven_day = travel(next_seven_day)
            
            #30 day
            temp = days[idx] + 30
            next_thirty_day = bisect.bisect_left(days, temp)
            thirty_day = travel(next_thirty_day)
            
            # min(costs[0]+helper(next_1), min(costs[1]+helper(next_2), costs[2]+helper(next_3)))
            
            
            return min(one_day + costs[0], min(seven_day + costs[1], thirty_day + costs[2]))
        
        return travel(0)
            
            
            
            
            
        