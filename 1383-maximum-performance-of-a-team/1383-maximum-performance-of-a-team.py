class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        person = list(zip(efficiency, speed))
        person.sort(reverse=True)
        minHeap = []
        runSum = 0
        maxPer = 0
        
        for eff, spd in person:
            curMin = eff
            
            heapq.heappush(minHeap, spd)
            runSum += spd
            
            if len(minHeap) > k:
                temp = heapq.heappop(minHeap)
                runSum -= temp
                
            curPer = curMin * runSum
            
            maxPer = max(maxPer, curPer)
            
        return maxPer % (10 ** 9 + 7)
    
    
            
            
        