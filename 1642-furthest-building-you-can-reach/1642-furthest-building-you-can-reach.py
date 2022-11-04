class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        hdiff = []
        for i in range (len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff > 0:
                heapq.heappush(hdiff, diff)
            if len(hdiff) > ladders:
                bricks -= heapq.heappop(hdiff)
            if bricks < 0:
                return i
        return len(heights) - 1