class RandomizedCollection:

    def __init__(self):
        self.numSet = defaultdict(set)
        self.numArr = []
    
    def insert(self, val: int) -> bool:
        existsBefore = len(self.numSet[val]) == 0
        
        self.numArr.append(val)
        self.numSet[val].add(len(self.numArr) - 1)
        
        return existsBefore
        

    def remove(self, val: int) -> bool:
        existsBefore = len(self.numSet[val]) > 0
        if not existsBefore:
            return False
        
        removeIdx = self.numSet[val].pop()
        if len(self.numArr) - 1 != removeIdx:
            # print(val, removeIdx, self.numArr, self.numSet)
            self.numArr[-1], self.numArr[removeIdx] = self.numArr[removeIdx], self.numArr[-1]
            self.numSet[self.numArr[removeIdx]].remove(len(self.numArr) - 1)
            self.numSet[self.numArr[removeIdx]].add(removeIdx)
            
            
        self.numArr.pop()
        
        return existsBefore

    def getRandom(self) -> int:
        randomIndex = random.randint(0, len(self.numArr) - 1)
        return self.numArr[randomIndex]