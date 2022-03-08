class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        
        for i in range(len(nums)):
            if len(heap) < k:
                heapq.heappush(heap, nums[i])
            elif heap[0] < nums[i]:
                heapq.heapreplace(heap,nums[i])
        
        return heap[0]
        
        