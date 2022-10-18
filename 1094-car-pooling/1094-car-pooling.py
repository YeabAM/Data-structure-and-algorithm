class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        numOfppl = [0 for _ in range(1002)]
        
        for current, beg, dest in trips:
            #people with number of capactiy is reserved at location beg
            numOfppl[beg + 1] += current
            #people with number of capactiy is dropped off at  location dest
            numOfppl[dest + 1] -= current
            
        for i in range(1, 1002):
            numOfppl[i] += numOfppl[i-1]
            
        for currentPpl in numOfppl:
            # print(currentPpl, capacity)
            if currentPpl > capacity:
                return False
            
        return True