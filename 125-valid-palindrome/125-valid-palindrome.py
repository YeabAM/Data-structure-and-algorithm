class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = []
        
        for l in s:
            if l.isalnum():
                string.append(l.lower())
                
        l = 0
        r = len(string) - 1
        # print(string)
        while l <= r:
            
            if string[l] != string[r]:
                # print("d")
                return False
            l += 1
            r -= 1
        
        return True
        