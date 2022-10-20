class RandomizedSet:

    def __init__(self):
        self.numSet = set()
        self.numArr = []
    
    def insert(self, val: int) -> bool:
        if val in self.numSet:
            return False
        self.numSet.add(val)
        self.numArr.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val in self.numSet:
            self.numSet.remove(val)
            return True
        
        return False
        
        

    def getRandom(self) -> int:
        randomIndex = random.randint(0, len(self.numArr) - 1)
        if self.numArr[randomIndex] not in self.numSet:
            self.numArr[-1], self.numArr[randomIndex] = self.numArr[randomIndex], self.numArr[-1]
            self.numArr.pop()
            return self.getRandom()
        return self.numArr[randomIndex]
    
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()