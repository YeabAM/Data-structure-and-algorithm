class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        N = len(plants)
        cur = 0
        
        for i in range(N):
                 
            if (capacity - cur) < plants[i]:
                cur = 0
                steps += (i * 2)
                
                
            cur += plants[i]
            steps += 1
            # print(i, cur, capacity, steps)
        
        return max(steps, N)
        