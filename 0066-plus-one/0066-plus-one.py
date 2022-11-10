class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        num = 0
        tenVal = 1
        
        for i in range(len(digits) -1 , -1, -1):
            currVal = tenVal * digits[i]
            num += currVal
            tenVal *= 10
            
        num += 1
        
        ans = []
        
        while num > 0:
            ans.append(num % 10)
            num = num // 10
            
        return ans[::-1]
        
        
        
            
        