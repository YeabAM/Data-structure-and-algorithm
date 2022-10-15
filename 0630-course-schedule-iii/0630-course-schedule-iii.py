class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        key = lambda a: a[1]
        courses.sort(key = key)
        curTime = 0
        heap = []
        
        for duration, lastDay in courses:
            curTime += duration
            heappush(heap, -duration)
            
            if curTime > lastDay and heap:
                top = -heappop(heap)
                curTime -= top
            
        return len(heap)