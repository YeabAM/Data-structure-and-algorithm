class Solution:
    def maxJump(self, stones: List[int]) -> int:
        if len(stones) == 2:
            return abs(stones[0] - stones[1])
        
        min_cost = float('-inf')
        
        for i in range(2, len(stones)):
            min_cost = max(min_cost, abs(stones[i] - stones[i-2]))
                           
        return min_cost
            
        