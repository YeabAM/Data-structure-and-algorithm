class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        
        prefixSum = [0 for _ in range(52)]
        
        for beg, end in ranges:
            prefixSum[beg] += 1
            prefixSum[end + 1] -= 1
            
        
            
        for i in range(1, len(prefixSum)):
            prefixSum[i] += prefixSum[i - 1]
            
        # print(prefixSum)
            
        for i in range(left, right+1):
            if prefixSum[i] == 0:
                return False
            
        return True
            
        