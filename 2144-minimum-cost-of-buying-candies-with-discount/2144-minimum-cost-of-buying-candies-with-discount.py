class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        
        cost.sort(reverse=True)
        
        total = 0
        i = 0
        
        
        while i < len(cost):
            total += sum(cost[i:i+2])
            
            i += 3

        return total
        
        