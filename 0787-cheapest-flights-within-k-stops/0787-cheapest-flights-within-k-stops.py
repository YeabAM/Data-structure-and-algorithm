class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        '''
        bellman-ford
        '''
        prices = [float('inf') for _ in range(n)]
        prices[src] = 0 
        for _ in range(k + 1):
            tempPrice = prices.copy()
            
            for s, d, cost in flights:
                if prices[s] == float('inf'):
                    continue
                    
                if tempPrice[d] > cost + prices[s]:
                    tempPrice[d] = cost + prices[s]

            prices = tempPrice
            
        return prices[dst] if prices[dst] != float('inf') else -1
            
        