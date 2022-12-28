class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        max_heap = []
        
        for pile in piles:
            heapq.heappush(max_heap, (-1 * pile))
            
        
        while k > 0:
            curr = heapq.heappop(max_heap)
            curr *= -1
            curr = ceil(curr / 2)
            heapq.heappush(max_heap, (-1 * curr))
            
            k -= 1
            
        remaining = 0
        
        while max_heap:
            remaining += -1 * (heapq.heappop(max_heap))
            
        return remaining
            
            
            
            
        