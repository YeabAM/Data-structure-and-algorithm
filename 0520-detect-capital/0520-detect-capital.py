class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        first_letter = False
        capital_count = 0
        
        for i in range(len(word)):
            if word[i].isupper():
                if i == 0:
                    first_letter = word[i].isupper()
                    
                capital_count += 1
                
        
        option_1 = capital_count == 0
        option_2 = capital_count == len(word)
        option_3 = (capital_count == 1) and (first_letter == True)
        
        # print(option_1, option_2, option_3)
        
        return option_1 or option_2 or option_3
                
            