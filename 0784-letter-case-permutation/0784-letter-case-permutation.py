class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        letter = []
        permutation = []
        
        def generateLetter(permuteValue):
            temp = list(s)
            
            for i in range(len(letter)):
                charPos = letter[i][0]
                if permuteValue & (1 << i):
                    temp[charPos] = temp[charPos].upper()
                else:
                    temp[charPos] = temp[charPos].lower()
                    
            newLetter = ''.join(temp)
            
            return newLetter
                    
        
        for idx, char in enumerate(s):
            if not char.isdigit():
                letter.append((idx, char))
                
        # print(letter)
                
        numOfPermuation =  2 ** len(letter)
        
        for i in range(numOfPermuation):
            possiblePermutation = generateLetter(i)
            
            permutation.append(possiblePermutation)
            
            
        
        return permutation
                
        
                
        