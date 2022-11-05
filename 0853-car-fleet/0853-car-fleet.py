class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        speedToDist = list(zip(position, speed))
        speedToDist.sort(reverse = True)
        
        fleetOfCars = None
        count = 0
    
        for i in range(len(speedToDist)):
            currSpeed = (target - speedToDist[i][0]) / speedToDist[i][1]
            if not fleetOfCars or fleetOfCars < currSpeed:
                count += 1
                fleetOfCars = currSpeed
                
        return count
                
            