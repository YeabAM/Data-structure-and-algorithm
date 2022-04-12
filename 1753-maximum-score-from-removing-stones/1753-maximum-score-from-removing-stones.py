class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        stones = [a, b, c]
        stones.sort()
        count = 0
        if stones[0] + stones[1] <= stones[2]:
            return stones[0] + stones[1]
        else:
            while stones[0] + stones[1] > stones[2]:
                stones[0] -= 1
                stones[1] -= 1
                count += 1
            
            return count + stones[0] + stones[1]
                
        