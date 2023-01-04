class Allocator:

    def __init__(self, n: int):
        self.memory = [0 for _ in range(n)]
        self.mid = defaultdict(set)

    def allocate(self, size: int, mID: int) -> int:
        #find left most memory
        # print(self.memory, 'before')
        remain = size
        left_most = 0
        # print(self.memory)
        for i in range(len(self.memory)):
            if remain == 0:
                break
                
            if self.memory[i] == 0:
                remain -= 1
                
            else:
                remain = size
                left_most = i+1
                
        if remain == 0:
            for j in range(left_most, left_most + size):
                self.memory[j] = mID
                self.mid[mID].add(j)
                
            # print(self.memory)
            return left_most
        
        else:
            return -1
                

    def free(self, mID: int) -> int:
        count = len(self.mid[mID])
        
        for unit in self.mid[mID]:
            self.memory[unit] = 0
            
        del self.mid[mID]
        
        return count
        


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)