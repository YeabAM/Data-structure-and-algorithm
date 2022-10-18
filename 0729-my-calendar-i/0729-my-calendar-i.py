class MyCalendar:

    def __init__(self):
        self.my_calandar = []
        
    def binary_search_left(self,search):
        left,right = 0,(len(self.my_calandar)*2)-1
        
        while left <= right:
            mid = left + (right-left)//2
            
            if self.my_calandar[mid//2][mid%2] < search:
                left = mid+1
            else:
                right = mid-1
                
        return left
    
    def overlap(self,start,end,start_position):
        num_events = len(self.my_calandar)
        is_end = start_position%2
        curr_event = start_position//2
        is_next_to_last_event = start_position >= 2*num_events
        
        if is_next_to_last_event:
            return False
        elif not is_end and end <= self.my_calandar[curr_event][0]:
            return False
        elif is_end and self.my_calandar[curr_event][1] <= start:
            if start_position + 1 < 2*num_events:
                if self.my_calandar[curr_event + 1][0] >= end :
                    return False
            else:
                return False
        return True
        
    def book(self, start: int, end: int) -> bool:
    
        if not self.my_calandar:
            self.my_calandar.append([start,end])
            return True
        
        self.my_calandar.sort()
        start_position = self.binary_search_left(start)
        
        if not self.overlap(start,end,start_position):
            self.my_calandar.append([start,end])
            return True
        else:
            return False
        
        
        

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)