class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        plant_grow = []
        total_seeds = len(plantTime)
        
        for i in range(total_seeds):
            plant_grow.append([growTime[i], plantTime[i]])
            
        plant_grow.sort(reverse = True)
        
        totalGrowTime = 0
        totalPlantTime = 0
        
        for grow, plant in plant_grow:
            totalPlantTime += plant
            totalGrowTime = max(totalGrowTime, totalPlantTime + grow)
            
        return totalGrowTime
    
            