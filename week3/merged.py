class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        intervals.sort()
        start = intervals[0][0]
        end = intervals[0][1]
        
        for i in range (1,len(intervals)):
            if intervals[i][0] <= end:
                end = max(intervals[i][1],end)
                
            else:
                merged.append([start,end])
                start = intervals[i][0]
                end = intervals[i][1]
                
        merged.append([start,end])
        
        return merged
            