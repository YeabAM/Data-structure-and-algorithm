class Solution:        
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = list(map(lambda x: int(x[:2]) * 60 + int(x[3:]), timePoints))
        minutes.sort()
        print(minutes)
        return min((y - x) % (24 * 60)  for x, y in zip(minutes, minutes[1:] + minutes[:1]))
