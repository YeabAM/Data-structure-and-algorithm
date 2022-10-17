class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        total = [0 for _ in range(n)]
        
        for beg, end, seat in bookings:
            total[beg -1] += seat
            if end < n:
                total[end] -= seat
                
        for i in range(1, len(total)):
            total[i] += total[i-1]
            
        return total
            