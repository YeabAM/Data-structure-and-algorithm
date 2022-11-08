class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        def isSet(i, n):
            return n & (1 << i) != 0
        
        def firstSetBit(binary):
            for i in range(32):
                if isSet(i, binary):
                    return i
                
                
        totalXor = 0
        
        for num in nums:
            totalXor ^= num
            
        firstBit = firstSetBit(totalXor)
        num1 = 0
        num2 = 0
        
        for num in nums:
            if isSet(firstBit, num):
                num1 ^= num
            else:
                num2 ^= num
        
        return [num1, num2]
                
        