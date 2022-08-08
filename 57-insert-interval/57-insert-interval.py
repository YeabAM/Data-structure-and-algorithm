class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        start = 0
        end = len(intervals) - 1
        mid = (start + end) // 2
        
        while start < end:
            if intervals[mid][0] == newInterval[0]:
                break
                
            elif intervals[mid][0] < newInterval[0]:
                if mid + 1 < len(intervals) and intervals[mid+1][0] > newInterval[0]:
                    break
                else:
                    start = mid + 1
            else:
                end = mid
            mid = (start + end) // 2
        if intervals[mid][1] < newInterval[0]:
            mid += 1
            intervals.insert(mid, newInterval)
        elif intervals[mid][0] > newInterval[0]:
            intervals.insert(mid, newInterval)
        else:
            intervals[mid][1] = max(newInterval[1], intervals[mid][1])
        length = len(intervals)
        
        while mid < length-1:
            if intervals[mid][1] < intervals[mid+1][0]:
                break
            else:
                intervals[mid][1] = max(intervals[mid][1], intervals[mid+1][1] )
                intervals.pop(mid+1)
                length -= 1
        
        return intervals