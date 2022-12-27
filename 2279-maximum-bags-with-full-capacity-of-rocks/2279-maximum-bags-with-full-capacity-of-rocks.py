class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        remaining = []
        
        
        for i in range(len(rocks)):
            remaining.append(capacity[i] - rocks[i])
            
        remaining.sort()
        
        for j in range(1, len(remaining)):
            remaining[j] += remaining[j-1]
            
        
    
        
        num_of_bags = bisect.bisect_right(remaining, additionalRocks)
        
        return num_of_bags
        
        
        
        