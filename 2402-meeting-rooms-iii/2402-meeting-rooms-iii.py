class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort() 
        book_count = [0 for _ in range(n)]
        
        ending_room = []
        free = [i for i in range(n)]
        heapq.heapify(free)
        
        last_time = 0
        
        for start, end in meetings:
            while ending_room and ending_room[0][0] <= start:
                ending, rooms = heapq.heappop(ending_room)
                heapq.heappush(free, rooms)
                
            if free:
                next_room = heapq.heappop(free)
                heapq.heappush(ending_room, (end, next_room))
                book_count[next_room] += 1
                
            else:
                delay = 0
                ends, room = heapq.heappop(ending_room)
                delay = ends - start
                book_count[room] += 1
                
                heapq.heappush(ending_room, (end + delay, room))
                
                        
                        
                         
                
        freq = 0
        # print(book_count)
        
        for j in range(n):
            if book_count[j] > book_count[freq]:
                freq = j
                
        return freq
        
                    
                    
                
                
        
        
        
        