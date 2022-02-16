class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        
        p1 = 0
        p2 = len(people) - 1
        minimum = 0
        
        while p1 <= p2:
            if people[p1] + people[p2] <= limit:
                p1 += 1
                p2 -= 1
                
            else:
                p2 -= 1
            
            minimum += 1
        
        return minimum
                
                
        