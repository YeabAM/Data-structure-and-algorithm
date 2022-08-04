class MyCalendar:

    def __init__(self):
        self.calendar = []
        

    def book(self, start: int, end: int) -> bool:
        startIdx = bisect.bisect(self.calendar, start)
        endIdx = bisect.bisect_left(self.calendar, end)
        
             
        if startIdx != endIdx or startIdx % 2 == 1:
            # print(startIdx, endIdx)
            return False
        else:
            self.calendar.insert(startIdx,start)
            self.calendar.insert(endIdx + 1, end)
            # print("cal", self.calendar)
            return True
        
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)