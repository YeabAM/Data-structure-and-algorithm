class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        jumps = [cost[0], cost[1]]
        
        for i in range(2, len(cost)):
            jumps.append(cost[i] + min(jumps[i-1], jumps[i-2]))
            
        return min(jumps[-1], jumps[-2])
        