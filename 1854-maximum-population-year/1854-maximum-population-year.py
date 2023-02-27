class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        year = 1950
        population = [0 for _ in range(2050 - 1950 + 1)]
        
        while year <= 2050:
            pos = year - 1950
            for b, d in logs:
                if b <= year and d > year:
                    population[pos] += 1
            year += 1
            
        max_pop = float('-inf')
        min_year = 0
        
        for i in range(2050 - 1950 + 1):
            if population[i] > max_pop:
                min_year = 1950 + i
                max_pop = population[i]
        
        return min_year
            
        
                
        