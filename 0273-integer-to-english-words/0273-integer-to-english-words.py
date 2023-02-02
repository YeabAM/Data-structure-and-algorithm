class Solution:
    def numberToWords(self, num: int) -> str:
    
        def change(num):
            words  = [
                    ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"],
                    ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"],
                    ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
                    
                 ]
        
            last_two = num % 100
            ones = last_two % 10

            letter = []


            if 10 <= last_two < 20:
                letter.append(words[1][ones])

            else:
                tens = last_two // 10
                if ones != 0:
                    letter.append(words[0][ones])

                if tens != 0:
                    letter.append(words[2][tens - 2])



            hundredth = num // 100

            if hundredth != 0:
                letter.append('Hundred')
                letter.append(words[0][hundredth])

            return " ".join(letter[::-1])
    
    
        ans = []
        index = 0
        
        if num == 0:
            return "Zero"
        
        words = ["Thousand","Million","Billion"]
        
        while num > 0:
            last_three = num % 1000
            read = change(last_three)
            # print(read,index)
            if index > 0 and read:
                read += " " + words[index - 1]
                # print(read)
            if read:    
                ans.append(read)
            
            num = num // 1000
            index += 1
            
        return " ".join(ans[::-1])
            
        
            
            
            
            