class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letterlogs = []
        digitslogs = []
        ans = []
        def checkLetter(word):
            for w in word:
                if w.isdigit():
                    return False
            return True
        
        for letter in logs:
            curr = list(letter.split())
            
            if checkLetter(curr[1:]):
                correct = curr[1:]
                letterlogs.append([' '.join(correct), curr[0]])
                
            else:
                digitslogs.append(" ".join(curr))
               
        letterlogs.sort()
        # print(letterlogs)  
        
        
        for word in letterlogs:
            # temp = [word[-1]] + word[:len(word) - 1]
            temp = ' '.join(word[::-1])
            ans.append(temp)
            
        for log in digitslogs:
            ans.append(log)
            
        return ans
            
            
            
            
                