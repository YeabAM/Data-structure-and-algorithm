class DetectSquares:

    def __init__(self):
        self.points = defaultdict(int)
        self.uniqes = set()

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1
        self.uniqes.add(tuple(point))
        

    def count(self, point: List[int]) -> int:
        x, y = point[0], point[1]
        count = 0
        
        for x2, y2 in self.uniqes:
            if (x, y) == (x2, y2):
                continue
                
            if x == x2:
                length = abs(y2 - y)
                count += self.points[(x2, y2)] * self.points[(x2 + length, y)] * self.points[(x2 + length, y2)]
                count += self.points[(x2, y2)] * self.points[(x2 - length, y)] * self.points[(x2 - length, y2)]
            
            elif y == y2:
                length = abs(x - x2)
                count += self.points[(x2, y2)] * self.points[(x2, length + y2)] * self.points[(x, length + y2)]
                count += self.points[(x2, y2)] * self.points[(x2, y2 - length)] * self.points[(x, y2 - length)]
                
        return count // 2

        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)

