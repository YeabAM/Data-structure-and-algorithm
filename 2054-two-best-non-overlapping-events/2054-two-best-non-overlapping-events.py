class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        
        l = []
        result = 0
        sumM = 0
        for i in range(len(events)):
            heapq.heappush(l, (events[i][1], events[i][2]))
                
                
            
            while l and l[0][0] < events[i][0]:
                
                end , val = heapq.heappop(l)
                
                sumM = max(sumM, val)
                
                
            result = max(result,sumM + events[i][2])
            
            
        return result