class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        if abs(dividend) == (2 ** 31)  and divisor == -1:
            return (2 ** 31) - 1
        
               
        isPositive = (dividend >=0 and divisor > 0) or (dividend < 0 and divisor < 0)
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        quotient = 0
        
        while (dividend - divisor) >= 0:
            count = 0
        
            while (dividend - (divisor << 1 << count)) >= 0:
    
                count += 1
                
            quotient += 1 << count
            dividend -= divisor << count
            
            
            
        if isPositive:
            return quotient
        else:
            return -1 * quotient
            
        
        
        