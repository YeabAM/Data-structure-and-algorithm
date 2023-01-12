class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        maxHeap = []
        score = 0
        
        for n in nums:
            heapq.heappush(maxHeap, -1 * n)
            
        
        while k > 0:
            curr = heapq.heappop(maxHeap)
            score += -1 * curr
            temp = -1 * curr
            transformed = ceil(temp / 3)
            heapq.heappush(maxHeap, transformed * -1)
            
            k -= 1
            
            
        return score
            
            