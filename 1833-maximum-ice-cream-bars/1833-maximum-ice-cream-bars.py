class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        
        costs.sort()
        total_coins = [0 for _ in range(len(costs))]
        total_coins[0] = costs[0]
        
        for i in range(1, len(costs)):
            total_coins[i] = total_coins[i-1] + costs[i]
            
        total_icecream = bisect.bisect_right(total_coins, coins)
        
        return total_icecream