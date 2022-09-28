class MedianFinder:

    def __init__(self):
        self.data1 = []
        self.data2 = []
        self.count = 0
    def addNum(self, num: int) -> None:
        self.count += 1
        if len(self.data1) > len(self.data2):
            temp = heappushpop(self.data1, num*-1)
            heappush(self.data2, temp*-1)
        
        else:
            temp = heappushpop(self.data2, num)
            heappush(self.data1, temp*-1)
            
        
    def findMedian(self) -> float:
        if self.count % 2 != 0:
            return self.data1[0] * -1
        else:
            return ((self.data1[0] * -1) + self.data2[0])/2