class Solution:
    def intToRoman(self, num: int) -> str:
        numeral = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        romans = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        
        ans = ""
        i = 0
        
        while num:
            ans += (num // numeral[i]) * romans[i]
            num %= numeral[i]
            i += 1
            
            
        return ans
        