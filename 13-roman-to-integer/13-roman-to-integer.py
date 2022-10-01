class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {}
        
        roman["I"] = 1
        roman["V"] = 5
        roman["X"] = 10
        roman["L"] = 50
        roman["C"] = 100
        roman["D"] = 500
        roman["M"] = 1000
        
        integer = 0
        
        for i in range(len(s) - 1):
            if roman[s[i]] >= roman[s[i+1]]:
                
                integer += roman[s[i]]
                # print("here", i, integer)
            else:
                integer -= roman[s[i]]
                # print("here2", i, integer)
                
        integer += roman[s[-1]]
        
        return integer
                
        