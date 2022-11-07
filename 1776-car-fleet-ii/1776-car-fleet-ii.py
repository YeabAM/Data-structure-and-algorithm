class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        result = []
        # cars that might collide with current car
        stack = []
        for position, speed in cars[::-1]:
            # then collision time is (x2 - x1) / (s1 - s2))
            while stack and (speed <= stack[-1][1] or (stack[-1][0] - position) / (speed - stack[-1][1]) >= stack[-1][2]):
                stack.pop()
            
            if not stack:
                stack.append((position, speed, math.inf))
                result.append(-1)
            # find collision time and add the car to the stack
            
            else:
                collideTime = (stack[-1][0] - position) / (speed - stack[-1][1])
                stack.append((position, speed, collideTime))
                result.append(collideTime)
        result.reverse()
        return result