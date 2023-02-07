class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        visited = set()
        curr = [0, 0]
        direction = 'N'
        
        for i in range(len(instructions)):
            direct = instructions[i]            
            if direct == 'G':
                if direction == 'N':
                    curr[1] += 1
                elif direction == 'S':
                    curr[1] -= 1
                elif direction == 'E':
                    curr[0] += 1
                elif direction == 'W':
                    curr[0] -= 1
                    
            elif direct == 'R':
                if direction == 'N':
                    direction = 'E'
                elif direction == 'S':
                    direction = 'W'
                elif direction == 'E':
                    direction = 'S'
                elif direction == 'W':
                    direction = 'N'
                    
            elif direct == 'L':
                if direction == 'N':
                    direction = 'W'
                elif direction == 'S':
                    direction = 'E'
                elif direction == 'E':
                    direction = 'N'
                elif direction == 'W':
                    direction = 'S'
                    
        if direction != 'N' or curr == [0, 0]:
            return True
        else:
            return False
                    
            
    
            
        