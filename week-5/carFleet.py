class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        Time = sorted([[position[i],(target-position[i]) / speed[i]]\
               for i in range(len(position))])
        stack = []
        
        for i, val in enumerate(Time):
            while stack and val[1] >= stack[-1]:
                stack.pop()
            stack.append(val[1])
            
        return len(stack)
                
                
                
            
        
        